import json
import xmltodict
from bs4 import BeautifulSoup

file_path = "" # file to be scraped

f = open(file_path)
data = f.read().decode('utf8')
data = BeautifulSoup(data).get_text()
print data