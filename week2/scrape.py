from secret import API_TOKEN
from lyricsgenius import Genius
import pandas as pd
import os

genius = Genius(API_TOKEN)
top_artists = pd.read_csv("top_artists.csv")
names = top_artists["artist"].values
ids = top_artists["artist_id"].values

for name, id in zip(names, ids):
    try:
        data = []

        print(name)
        returned = genius.search_artist(artist_name=name, artist_id=id, max_songs=100, per_page=2)

        for song in returned.songs:
            data.append([
                song.artist,
                song.id,
                song.lyrics_owner_id,
                song.primary_artist.id,
                song.primary_artist.name,
                song.song_art_image_thumbnail_url,
                song.title,
                song.url,
                song.stats.pageviews,
                song.lyrics])

        pd.DataFrame(data, columns=["artist", "id", "lyrics_owner_id", "primary_artist_id",
        "primary_artist_name", "song_art_image_thumbnail_url", "title", "url", "pageviews", "lyrics"]).to_csv(f"./songs/{name}.csv", index=False)
    except:
        continue

#print(dir(genius))
#print(genius.search_artist.__doc__)