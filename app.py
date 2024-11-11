import os
from flask import Flask, render_template, request
import pandas as pd
import pickle
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)

def load_model():
    # Get the path to the models folder within the project directory
    project_folder = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    model_folder = os.path.join(project_folder, 'models')
    model_path = os.path.join(model_folder, 'recommendation_model.pkl')

    # Load the model and data
    with open(model_path, 'rb') as file:
        cosine_sim, data = pickle.load(file)
    return cosine_sim, data

cosine_sim, data = load_model()

def get_recommendations(title, num_recommendations=5):
    # Find the index of the song
    indices = data[data['title'].str.lower() == title.lower()].index
    if indices.empty:
        return None
    idx = indices[0]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # Exclude the input song itself
    song_indices = [i[0] for i in sim_scores]

    # Return the top recommendations
    return data.iloc[song_indices][['title', 'artist', 'genre', 'year']]

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    error_message = None
    if request.method == 'POST':
        song_title = request.form['song_title']
        recommendations = get_recommendations(song_title)
        if recommendations is None or recommendations.empty:
            error_message = "Song not found. Please try another title."
            recommendations = None  # Set to None if there are no results

    return render_template('index.html', recommendations=recommendations, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
