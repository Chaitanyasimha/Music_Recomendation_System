## Project Structure

The following is the structure of the **Music Recommendation System** project, designed to provide a clear overview of the files and folders used. This README will explain the purpose and functionality of each component, ensuring easy navigation through the project files.
- this is how we have to create the folder placing the apropriate files in that folders in your project directory


music_recommendation_system/
├── data/                       # Folder for data storage and raw datasets
│   ├── processed_data.csv      # Processed synthetic data used in the project
│   └── database_schema.sql     # SQL schema file for MySQL database structure
├── scripts/                    # Python scripts for data processing and model training
│   ├── generate_synthetic_data.py # Script to generate synthetic song data
│   ├── data_preprocessing.py   # Script to clean and preprocess data
│   ├── model_training.py       # Script to train the recommendation model
│   ├── database_operations.py  # Script for MySQL database operations
│   └── recommendation.py       # Script to generate song recommendations
├── templates/                  # HTML templates for the Flask web interface
│   └── index.html              # Main HTML page for the user interface
├── models/                     # Folder for saving the trained model
│   └── recommendation_model.pkl # Serialized model file
├── config.py                   # Configuration file for secure database credentials
├── app.py                      # Flask app to run the web interface
├── requirements.txt            # List of required packages and dependencies
└── README.md                   # Project documentation

---

### Detailed Structure and File Descriptions

1. **`data/`**: This folder contains the primary data files used in the project.
   - **`processed_data.csv`**: A CSV file containing the processed synthetic song data. This file is generated by the `generate_synthetic_data.py` script and holds song information such as `title`, `artist`, `genre`, and `year`.
   - **`database_schema.sql`**: This file defines the structure of the MySQL database used for storing song data. It includes table definitions necessary for setting up the project’s database schema in MySQL.

2. **`scripts/`**: This folder contains essential scripts used for generating data, preprocessing, training the recommendation model, and managing database operations.
   - **`generate_synthetic_data.py`**: This script generates synthetic song data and saves it to `processed_data.csv` in the `data` folder. It simulates real-world song information, allowing the recommendation system to operate without relying on an external API.
   - **`data_preprocessing.py`**: This script cleans and preprocesses the raw data to ensure data quality before database insertion. It handles missing values, duplicate removal, and formatting, saving the cleaned data back to `processed_data.csv`.
   - **`model_training.py`**: This script trains a content-based recommendation model using Scikit-learn. It calculates cosine similarity between songs based on `artist` and `genre` attributes and saves the trained model to `recommendation_model.pkl`.
   - **`database_operations.py`**: This script manages data insertion into the MySQL database. It connects to the database, reads data from `processed_data.csv`, and populates the `songs` table defined in `database_schema.sql`.
   - **`recommendation.py`**: This script loads the trained model and retrieves song recommendations based on a specified song title. It can be executed independently for testing recommendation results or integrated into the web app.

3. **`templates/`**: This folder holds HTML templates used by the Flask web application.
   - **`index.html`**: The primary HTML file for the user interface. It allows users to input a song title and displays recommended songs returned by the system.

4. **`models/`**: This folder stores the trained recommendation model.
   - **`recommendation_model.pkl`**: A serialized file containing the trained cosine similarity model. The model is used by the recommendation system to find and rank similar songs.

5. **`config.py`**: This configuration file securely stores database credentials such as `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME`. By separating credentials, it keeps sensitive information out of the main project files.

6. **`app.py`**: The main Flask application file. This script runs the web server, handles user requests, and displays song recommendations based on input provided via the web interface.

7. **`requirements.txt`**: This file lists all the necessary Python packages and dependencies required to run the project. It can be used to install dependencies in a virtual environment by running `pip install -r requirements.txt`.

8. **`README.md`**: The project documentation file. This README provides an overview of the project, instructions for setup, and guidance for usage.


## Project Overview

The **Music Recommendation System** is a content-based recommendation engine built to suggest songs based on an input song title. This system uses a synthetic dataset that simulates real-world song metadata and relies on a cosine similarity model trained on `artist` and `genre` attributes. The project includes a Flask-based web interface for an interactive user experience, making it easy to input a song title and view recommended songs.

### Key Features

- **Content-Based Recommendations**: The system suggests songs similar to the input song based on shared `artist` and `genre` attributes.
- **Synthetic Data Generation**: Generates realistic synthetic data, allowing the recommendation system to work without needing external APIs.
- **Flask Web Interface**: A user-friendly web application for inputting song titles and viewing recommendations.
- **MySQL Database Integration**: The synthetic data is stored in a MySQL database, allowing scalable storage and efficient querying.

---

## Installation and Setup

To set up the **Music Recommendation System**, follow these steps:

### Prerequisites

1. **Python 3.7+**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **MySQL**: Install MySQL and create a new database named `music_recommendation`. Alternatively, you can adjust the database name in `config.py` if you choose a different name.
3. **Git** (optional): To clone the project from GitHub.

### Step 1: Clone the Repository

Clone the repository (if using GitHub):

```bash
git clone https://github.com/your_username/music_recommendation_system.git
cd music_recommendation_system
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

Creating a virtual environment isolates the project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### Step 3: Install Dependencies

Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database Credentials

In the `config.py` file, update the database credentials with your MySQL details:

```python
# config.py

DB_HOST = "localhost"
DB_USER = "your_mysql_username"         # Replace with your MySQL username
DB_PASSWORD = "your_mysql_password"     # Replace with your MySQL password
DB_NAME = "music_recommendation"         # Ensure this matches the name of your MySQL database
```

### Step 5: Set Up the MySQL Database

1. **Create the Database**:
   - Open MySQL and create a new database:

     ```sql
     CREATE DATABASE music_recommendation;
     ```

2. **Run the Database Schema**:
   - Use the `database_schema.sql` file located in the `data/` folder to create the required tables in your database:

     ```bash
     mysql -u your_mysql_username -p music_recommendation < data/database_schema.sql
     ```

3. **Populate the Database**:
   - Run the `database_operations.py` script to load data from `processed_data.csv` into the MySQL database:

     ```bash
     python scripts/database_operations.py
     ```

This script will connect to your MySQL database, read the `processed_data.csv` file, and populate the `songs` table with synthetic data.

---

### Step 6: Generate the Recommendation Model

To build the recommendation model, execute the `model_training.py` script:

```bash
python scripts/model_training.py
```

This will:
- Load the data from the MySQL database.
- Train a content-based recommendation model using cosine similarity on `artist` and `genre` attributes.
- Save the trained model as `recommendation_model.pkl` in the `models/` folder.

---

### Step 7: Start the Flask Application

Once the model is trained, you can start the Flask application to interact with the recommendation system:

```bash
python app.py
```

By default, the Flask app will run locally at `http://127.0.0.1:5000/`. Open this URL in your browser to access the application.

---

## Usage

1. **Enter a Song Title**:
   - On the main page, enter a song title from the dataset (e.g., "Echoes of Eternity 42") into the input box and click **Get Recommendations**.
   
2. **View Recommendations**:
   - The system will return a list of recommended songs that share similar `artist` and `genre` attributes, ranked by similarity.
   
3. **Error Handling**:
   - If a song title isn’t found, an error message will display, prompting you to try another title.

---

## Project Dependencies

This project uses the following packages and technologies:

- **Python**: Core language for scripting and data processing.
- **Flask**: For creating the web interface.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For training the content-based recommendation model.
- **MySQL**: As the database for storing song data.
- **mysql-connector-python**: For connecting to the MySQL database from Python.
- **Jinja2**: For rendering HTML templates in Flask.

To install all dependencies, use the `requirements.txt` file as mentioned in the setup steps.

---

## Portfolio Links

For more of my work, please visit:

- **GitHub Portfolio**: [https://github.com/Chaitanyasimha/Portfolio](https://github.com/Chaitanyasimha/Portfolio)
- **Website Portfolio**: [https://chaitanyasimha.github.io/Portfolio/](https://chaitanyasimha.github.io/Portfolio/)
