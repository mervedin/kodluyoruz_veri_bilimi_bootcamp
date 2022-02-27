from secret import API_TOKEN
from lyricsgenius import Genius
import pandas as pd

genius = Genius(API_TOKEN)
#print(genius.charts.__doc__)
data = []
i = 1
while i is not None:
    charts = genius.charts(time_period='all_time',chart_genre='all', per_page=50, type_="artists", page=i)
    for item in charts["chart_items"]:
        data.append([item["item"]["name"], item["item"]["id"], item["item"]["url"]])
    i = charts["next_page"]
    print(charts["next_page"])
pd.DataFrame(data, columns=["artist", "artist_id", "artist_url"]).to_csv("top_artists.csv", index=False)

   
   
   
