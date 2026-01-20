import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(".titleline a")
subtexts = soup.select(".subtext")

li = []

for idx, link in enumerate(links):
    title = link.get_text()
    href = link.get("href", None)

    if idx < len(subtexts):
        score_tag = subtexts[idx].select_one(".score")
        score = int(score_tag.get_text().split()[0]) if score_tag else 0
    else:
        score = 0

    if score > 100:
        li.append((title, href, score))

li.sort(key=lambda x: x[2], reverse=True)

pprint.pprint(li)
