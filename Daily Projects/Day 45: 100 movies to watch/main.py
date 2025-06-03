import os.path

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
FILENAME = "movies.txt"

response = requests.get(URL)
article = response.text

soup = BeautifulSoup(article, "html.parser")

names = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
names.reverse() # reverse the list from 1-100

if not os.path.isfile(FILENAME):
    new_file = open(FILENAME, "x")

with open(FILENAME, "w") as file:
    for name in names:
        file.write(f"{name}\n")

print(f"The file {FILENAME} was created or overwritten.")
