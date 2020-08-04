from bs4 import BeautifulSoup, NavigableString, Tag
import requests

URL = "https://movie.naver.com/movie/running/current.nhn"

req = requests.get(URL)
soup = BeautifulSoup(req.text, "html.parser")

movie_section = soup.select(
    "#content > div.article > div.obj_section > div.lst_wrap > ul > li")
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1)

for contents in movie_section:
    a_tag = contents.select_one('dl > dt > a')
    title = a_tag.getText()
    number = a_tag.get("href").split('=')[1]
    
    moive_data = {
        'title' : title,
        'number' : number
    }

    print(title, number)


# https://github.com/Liebe97/first_repository/blob/master/scraping/news3.py