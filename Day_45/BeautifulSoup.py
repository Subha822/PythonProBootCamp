from bs4 import BeautifulSoup
import lxml
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")

articles = soup.findAll(name="a", class_="storylink")
article_upvotes = soup.findAll(name="span",class_="score")
text = []
link = []
upvote = []
for i in articles:
    i.getText()
    text.append(i.getText())
    i.get("href")
    link.append(i.get("href"))
for j in article_upvotes:
    j.getText()
    upvote.append(int(j.getText().split()[0]))

# print(text)
# print(link)
# print(upvote)

max_upvote = max(upvote)
# print(max_upvote)
index = upvote.index(max_upvote)
print("TITLE :",text[index])
print("LINK :",link[index])



# article_title = soup.find(name="a", class_="storylink")
# article_link = article_title.get("href")
# article_upvote = soup.find(name="span",class_="score")
#
# print(article_title.getText())
# print(article_link)
# print(article_upvote.getText())



# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.p)
# find_all_anchor_tags = soup.findAll(name="a")
# print(find_all_anchor_tags)
# for i in find_all_anchor_tags:
#     print(i.getText())
#     print(i.get("hrsef"))
# heading_id = soup.find(name="h1",id="name")
# print(heading_id)
# heading_class = soup.find(name="h3", class_="heading")
# print(heading_class)
# anchor_tag = soup.select_one(selector="p a")
# print(anchor_tag)
# anchor_tag = soup.select_one(selector="#name")
# print(anchor_tag)
# heading = soup.select(".heading")
# print(heading)