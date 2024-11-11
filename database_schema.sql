CREATE DATABASE music_recommendation;
USE music_recommendation;

CREATE TABLE songs (
    song_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    genre VARCHAR(100),
    year INT
);

CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    song_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
);
