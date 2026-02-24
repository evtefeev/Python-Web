import sqlite3

# Створення або підключення до бази даних
connection = sqlite3.connect("songs.db")
cursor = connection.cursor()


songs = [
    "Imagine Dragons - Believer",
    "Ed Sheeran - Shape of You",
    "Beyoncé - Halo",
    "The Weeknd - Blinding Lights",
    "Coldplay - Viva La Vida",
    "Adele - Rolling in the Deep",
    "Maroon 5 - Sugar",
    "OneRepublic - Counting Stars",
    "Taylor Swift - Shake It Off",
    "Post Malone - Circles",
    "Shawn Mendes - Treat You Better",
    "Justin Bieber - Love Yourself",
    "Dua Lipa - Don't Start Now",
    "Lady Gaga - Shallow",
    "Billie Eilish - Bad Guy",
    "Bruno Mars - Uptown Funk",
    "Harry Styles - Watermelon Sugar",
    "Chainsmokers - Closer",
    "Linkin Park - Numb",
    "Katy Perry - Roar",
    "Sam Smith - Stay With Me"
]

def create():
    # Створення таблиці для збереження пісень
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artist TEXT NOT NULL,
        song_name TEXT NOT NULL   
    )
    ''')

    print("Таблиця 'songs' створена успішно!")
    connection.commit()


def fill():
    # Додавання даних до таблиці
    for song in songs:
        artist, song_name = song.split(' - ')
        cursor.execute('''
        INSERT INTO songs (artist, song_name)
        VALUES (?, ?)
        ''', (artist, song_name))
    connection.commit()
    print("Таблиця 'songs' заповнена!")


def get():
    # Виведення всіх записів із таблиці
    cursor.execute("SELECT * FROM songs")
    return cursor.fetchall()


def songs_to_list(songs):
    res = []
    for song in songs:
        res.append(f"{song[1]} -  {song[2]}")
    return(res)


def main():
    # create()
    # fill()
    print(songs_to_list(get()))
    connection.close()

    # print("Дані з таблиці 'songs':")
    # for data in get():
    #     print(data)

    # print(songs_to_list(get()))


if __name__ == "__main__":
    main()