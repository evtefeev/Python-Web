from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import database
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(title="Music Chart API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Song(BaseModel):
    id: int
    artist: str
    song_name: str


@app.get("/songs", response_model=List[Song])
def get_songs():
    songs = database.get()
    return [Song(id=s[0], artist=s[1], song_name=s[2]) for s in songs]


@app.get("/search", response_model=List[Song])
def search(query: str = Query(..., min_length=1)):
    songs = database.search_songs(query)
    return [Song(id=s[0], artist=s[1], song_name=s[2]) for s in songs]




if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    )