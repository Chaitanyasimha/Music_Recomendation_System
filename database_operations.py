import mysql.connector
import pandas as pd
import os
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def connect_to_db():
    # Connect to the MySQL database using credentials from config.py
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection

def insert_data_into_db():
    # Connect to the database
    connection = connect_to_db()
    cursor = connection.cursor()

    # Define the path to the processed data
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    input_path = os.path.join(data_folder, 'processed_data.csv')

    # Load the processed data
    data = pd.read_csv(input_path)
    print("Data loaded successfully for import.")

    # Insert data into the 'songs' table
    for _, row in data.iterrows():
        sql = """
            INSERT INTO songs (title, artist, genre, year)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (row['title'], row['artist'], row['genre'], row['year']))

    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()
    print("Data imported successfully into the database.")

# Run the data import function
if __name__ == "__main__":
    insert_data_into_db()
