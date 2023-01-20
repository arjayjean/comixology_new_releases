import requests
from bs4 import BeautifulSoup
import subprocess
subprocess.run('clear')

URL = 'https://www.amazon.com/kindle-dbs/comics-store/home/?ref_=topnav_storetab_kstore_cmx&_encoding=UTF8&slot=desktop-atf-10'
response = requests.get(URL)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# print(type(response))