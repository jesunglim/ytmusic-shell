import requests
import pandas as pd
from bs4 import BeautifulSoup 

keyword = input('검색어: ')

req = requests.get('https://www.youtube.com/results?search_query=' + keyword)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
)
title = []
url = []

for idx in my_titles:
    title.append(idx.text)
    url.append(idx.get('href'))


title_list = pd.DataFrame(url, columns = ['url'])
title_list['title'] = title
title_list