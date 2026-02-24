import database


SONGS = "$SONGS$"


def render(text: str) -> str:
    if SONGS in text:
        songs = database.songs_to_list(database.get())
        text = text.replace(SONGS, str(songs))
    
    return text