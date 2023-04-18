# beautiful soup lib from site data extraction
from bs4 import BeautifulSoup
from requests_html import HTMLSession

#
# response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
# content = response.text

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "The 100 Best Movies Of All Time _ Movies _ Empire.html"


# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()

    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)


# download page to local file
get_web_page()

with open("The 100 Best Movies Of All Time _ Movies _ Empire.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

title_tags = soup.find_all(name="h3", class_="jsx-4245974604")
movie_titles = {(title.get_text().split()[0])[:-1]: title.get_text()[3:] for title in title_tags}
# print(f"{movie_titles}\n")
print(f"The best movie of al times: {movie_titles['1']}")

