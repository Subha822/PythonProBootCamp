import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id="82716a64dfb6402a9a023b27612dfbd9",
        client_secret="170b3ec4ab864d898dfe6155746c566a",
        show_dialog=True,
        cache_path="token.txt",
        username="Billboard to Spotify",
    )
)
user_id = sp.current_user()["id"]
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]
URL = "https://www.billboard.com/charts/hot-100/"+date+"/"
response = requests.get(URL,headers=header)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
titles = soup.select("li ul li h3")
title = []
for i in titles:
    i.getText()
    title.append(i.getText().strip())
song_uris = []
for song in title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# https://open.spotify.com/playlist/08YX6BhFSIep14qLquLV3N