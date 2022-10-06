from ast import Div
from pydoc import classify_class_attrs
from urllib import request
import requests
from bs4 import BeautifulSoup
req= requests.get("https://www.truecaller.com/search/in/9866486658")
soup= BeautifulSoup(req.content, "html.parser")
#print(soup.prettify)
s=s
print(s)