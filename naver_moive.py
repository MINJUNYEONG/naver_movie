from bs4 import BeautifulSoup, NavigableString, Tag
import requests

URL = "https://movie.naver.com/movie/running/current.nhn"

req = requests.get(URL)
soup = BeautifulSoup(req.text, "html.parser")

movie_section = soup.select(
    "#content > div.article > div.obj_section > div.lst_wrap > ul > li")

movie_data = []

for contents in movie_section:
    a_tag = contents.select_one('dl > dt > a')
    movie_data.append({'title':a_tag.getText(), 'number':a_tag.get("href").split('=')[1]}) 

print(movie_data)

