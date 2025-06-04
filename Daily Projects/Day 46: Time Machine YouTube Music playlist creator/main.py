import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic, OAuthCredentials
from dotenv import load_dotenv

load_dotenv()

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=os.environ["CLIENT_ID"], client_secret=os.environ["CLIENT_SECRET"]))

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=url, headers=header)
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")
all_songs = soup.select("li ul li h3")
all_artists = soup.select("h3 ~ span")

songs = [song.getText().strip() for song in all_songs]
artists = [artist.getText().strip() for artist in all_artists]

# creating a playlist on YouTube music
playlistId = ytmusic.create_playlist(title=f"Throwback to {date}", description=f"Top songs on Billboard on {date}.")
for artist, song in zip(artists, songs):
    search_results = ytmusic.search(f"{artist} {song}")

    try:
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
        print("Song added.")
    except KeyError:
        print("Key Error.")


print("Playlist created!")
