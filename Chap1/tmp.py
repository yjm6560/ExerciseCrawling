from urllib.request import urlopen
from bs4 import BeautifulSoup


"""
    How to use urlopen funct of urllib library and BeautifulSoup
"""
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
