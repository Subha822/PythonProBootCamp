import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")

title = soup.findAll(name="h3", class_="title")
title_array = []
for i in title:
    title_array.append(i.getText())

values = title_array[::-1]
with open("movies.txt",mode="w") as file:
    for j in values:
        file.write(f"{j}\n")