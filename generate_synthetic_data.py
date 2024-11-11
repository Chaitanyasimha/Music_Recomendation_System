import os
import pandas as pd
import random

# Define lists of possible values for generating synthetic data
titles = ['Echoes of Eternity', 'Whispers in the Wind', 'Shadows of the Night', 'Rhythms of the Heart']
artists = ['The Harmonics', 'Echo Ensemble', 'Serenity Sounds', 'The Vibrations']
genres = ['Pop', 'Rock', 'Jazz', 'Classical']
years = list(range(1980, 2023))

def generate_data(num_entries):
    data = {
        'title': [],
        'artist': [],
        'genre': [],
        'year': []
    }

    for _ in range(num_entries):
        title = random.choice(titles) + ' ' + str(random.randint(1, 100))
        artist = random.choice(artists)
        genre = random.choice(genres)
        year = random.choice(years)
        
        data['title'].append(title)
        data['artist'].append(artist)
        data['genre'].append(genre)
        data['year'].append(year)
    
    df = pd.DataFrame(data)

    # Save data to the 'data' folder
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    output_path = os.path.join(data_folder, 'processed_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Synthetic dataset generated with {num_entries} entries and saved at {output_path}")

# Generate the dataset with a specified number of entries
if __name__ == "__main__":
    generate_data(2000)  # You can adjust the number to suit your needs
