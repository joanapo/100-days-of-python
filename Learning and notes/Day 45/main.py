from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

print(soup.title.getText())
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.find(name="a").get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

most_upvoted = article_upvotes.index(max(article_upvotes))

print(article_texts[most_upvoted])
print(article_links[most_upvoted])
print(article_upvotes[most_upvoted])