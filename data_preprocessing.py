import os
import pandas as pd

def load_and_clean_data():
    # Define the path to the data folder and dataset
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    input_path = os.path.join(data_folder, 'processed_data.csv')

    # Load the synthetic data
    data = pd.read_csv(input_path)
    print("Original dataset loaded.")

    # Remove any duplicate rows based on 'title' and 'artist'
    initial_count = len(data)
    data.drop_duplicates(subset=['title', 'artist'], inplace=True)
    final_count = len(data)
    print(f"Removed {initial_count - final_count} duplicate entries, if any.")

    # Save the cleaned data
    data.to_csv(input_path, index=False)
    print("Data preprocessing complete. Cleaned data saved back to 'processed_data.csv'.")

# Run the preprocessing function
if __name__ == "__main__":
    load_and_clean_data()
