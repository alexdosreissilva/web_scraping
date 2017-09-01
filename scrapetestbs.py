#coding=utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    if html is None:
        print("URL is not found")
    else:
        try:
            bsObj = BeautifulSoup(html.read(), 'html.parser')
            if bsObj.h1 == None:
                print("Tag was not found")
            else:
                print(bsObj.h1)
        except AttributeError as e:
            print("Tag was not found")
except HTTPError as e:
    print(e)
