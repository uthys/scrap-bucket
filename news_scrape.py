import re
import urllib.request
import traceback

from bs4 import BeautifulSoup

url = "https://abcnews.go.com/Health/Coronavirus"
html = urllib.request.urlopen(url)
htmlParse = BeautifulSoup(html, 'html.parser')

for link in htmlParse.find_all('a',attrs={'href': re.compile("^https://abcnews.go.com/GMA")}):  
    links = []
    if link.has_attr('href'):
        links.append(link['href'])
        for sublink in links:
            htmlParse = BeautifulSoup(urllib.request.urlopen(sublink), 'html.parser')

            for paragraphs in htmlParse.find_all('p'):
                try:
                    with open('%s.txt'%link.get_text(), 'a') as  f:
                        f.write('%s'%paragraphs.get_text())
                except:
                    print(traceback.format_exc())
            f.close()