# beautiful soup lib from site data extraction
from bs4 import BeautifulSoup
import requests
#
# response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
# content = response.text
with open("The 100 Best Movies Of All Time _ Movies _ Empire.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

title_tags = soup.find_all(name="h3", class_="jsx-4245974604")
movie_titles = {title.get_text().split()[0]: ''.join(title.get_text().split()[1:]) for title in title_tags}
print(movie_titles["100)"])

