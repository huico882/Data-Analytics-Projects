# Data Analytics Projects
This is a collection of data analytic projects I have completed. Some tools used include SQL, Excel, Python, and Tableau.

## Projects
- Billboard Top 100 Analysis of Audio Features


### Billboard Top 100 Analysis of Audio Features

#### Process
1. Download the files Billboard (includes Billboard Top 100 since 1958) and the Spotify audio features from [Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/top-100-billboard).
2. Download SQLite to join both sheets using the identifiers: song and performers. Include features such as key, tempo, and danceability with data such as the date, and week position that were on Billboard.
3. Once both CSV files have been imported to SQLite, Use the following code to join and create a new table called 'billboard_audio_features'
   ```
       CREATE TABLE billboard_audio_features AS
       SELECT
        b.*,
        s.tempo,
        s.key,
        s.danceability,
            s.energy,
            s.loudness,
            s.speechiness,
            s.acousticness,
            s.instrumentalness,
            s.liveness,
            s.valence
    FROM billboard AS b
    LEFT JOIN audio_features AS s
        ON b.song = s.song
        AND b.performer = s.performer;
   ```
4. Once the SQL code has been executed and the table has been created, export the table from SQLite and import the CSV file to Tableau.
5. From here, create any analysis and visuals for dashboard!
