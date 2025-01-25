from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")
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