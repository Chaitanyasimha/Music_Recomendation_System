
import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

def connect_to_db():
    # Update these credentials based on your MySQL setup
    connection = mysql.connector.connect(
        host="riserVICTOR",        # Adjust as necessary
        user="simha",             # Your MySQL username
        password="simha",         # Your MySQL password
        database="music_recommendation"
    )
    return connection

def load_data_from_db():
    # Connect to the database and fetch data from the 'songs' table
    connection = connect_to_db()
    query = "SELECT * FROM songs"
    data = pd.read_sql(query, connection)
    connection.close()
    return data

def create_similarity_model(data):
    # Combine relevant features into a single string for each song
    data['combined_features'] = data['artist'] + ' ' + data['genre']

    # Create a count matrix based on combined features
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['combined_features'])

    # Compute cosine similarity between songs
    cosine_sim = cosine_similarity(count_matrix)

    # Get the path to the models folder within the project directory
    project_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    model_folder = os.path.join(project_folder, 'models')
    os.makedirs(model_folder, exist_ok=True)  # Ensure the directory exists
    model_path = os.path.join(model_folder, 'recommendation_model.pkl')

    # Save the model and data indices
    with open(model_path, 'wb') as file:
        pickle.dump((cosine_sim, data), file)
    print(f"Recommendation model trained and saved at {model_path}")

# Run the model creation function
if __name__ == "__main__":
    data = load_data_from_db()
    create_similarity_model(data)
