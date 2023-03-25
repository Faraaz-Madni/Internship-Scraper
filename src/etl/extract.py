from urllib.request import urlopen
from bs4 import BeautifulSoup

html_file = urlopen('https://internshala.com')
bs = BeautifulSoup(html_file.read(),'html.parser')
print(bs)