CREATE TABLE IF NOT EXISTS Singers (singer_id SERIAL PRIMARY KEY, singer_name VARCHAR);
CREATE TABLE IF NOT EXISTS Genres (genre_id SERIAL PRIMARY KEY, genre_name VARCHAR);
CREATE TABLE IF NOT EXISTS Singers_Genres (id SERIAL PRIMARY KEY, singer_id INTEGER REFERENCES Singers(singer_id), singer_genre_id INTEGER REFERENCES Genres(genre_id));
CREATE TABLE IF NOT EXISTS Albums (album_id SERIAL PRIMARY KEY, album_name VARCHAR, album_year INTEGER);
CREATE TABLE IF NOT EXISTS Singers_Albums (id SERIAL PRIMARY KEY, singer_id INTEGER REFERENCES Singers(singer_id), album_id INTEGER REFERENCES Albums(album_id));
CREATE TABLE IF NOT EXISTS Soundtracks (soundtrack_id SERIAL PRIMARY KEY, soundtrack_name VARCHAR, soundtrack_length INTERVAL, soundtrack_album_id INTEGER REFERENCES Albums(album_id));
CREATE TABLE IF NOT EXISTS Mixes (mix_id SERIAL PRIMARY KEY, mix_name VARCHAR, mix_year INTEGER);
CREATE TABLE IF NOT EXISTS Mixes_Soundtracks (id SERIAL PRIMARY KEY, mix_id INTEGER REFERENCES Mixes(mix_id), soundtrack_id INTEGER REFERENCES Soundtracks(soundtrack_id));