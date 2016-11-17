import json
import xmltodict
from bs4 import BeautifulSoup

file_path = "/Users/apple/Documents/Python/GRETIL-Prakrit/Prakrit/"

# file to be scraped
file_name = ""

# output file name
out_file_name = ""

f = open(file_path+file_name)
data = f.read().decode('utf-8')
data = BeautifulSoup(data, "html5lib").get_text().encode('utf-8')

out = open(file_path+out_file_name, "w+")
out.write(data)