import pandas as pd
import numpy as np
import pickle
import os

def load_model():
    # Define the path to the saved model within the project folder
    model_folder = os.path.join(os.path.dirname(__file__), '..', 'models')
    model_path = os.path.join(model_folder, 'recommendation_model.pkl')

    # Load the model and data
    with open(model_path, 'rb') as file:
        cosine_sim, data = pickle.load(file)
    return cosine_sim, data

def get_song_index(title, data):
    # Find the index of the song with the specified title
    try:
        return data[data['title'] == title].index.values[0]
    except IndexError:
        print(f"Song '{title}' not found in the database.")
        return None

def recommend_songs(title, num_recommendations=5):
    cosine_sim, data = load_model()
    song_idx = get_song_index(title, data)
    
    if song_idx is None:
        return []

    # Get pairwise similarity scores for the given song
    sim_scores = list(enumerate(cosine_sim[song_idx]))
    # Sort songs based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get indices of the most similar songs
    sim_scores = sim_scores[1:num_recommendations+1]  # Skip the first item as it's the same song
    song_indices = [i[0] for i in sim_scores]

    # Return the recommended songs as a DataFrame
    return data.iloc[song_indices][['title', 'artist', 'genre', 'year']]

# Example usage
if __name__ == "__main__":
    song_title = "Echoes of Eternity 42"  # Replace with a song title from your dataset
    recommendations = recommend_songs(song_title)
    
    if not recommendations.empty:
        print(f"Recommendations for '{song_title}':\n")
        print(recommendations.to_string(index=False))
