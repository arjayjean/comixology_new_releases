import requests
from bs4 import BeautifulSoup
import subprocess
import csv
import datetime
import boto3
subprocess.run('clear')

"""Extracting data from Amazon's Comixology page using Beautiful Soup"""
URL = 'https://www.amazon.com/kindle-dbs/comics-store/home/?ref_=topnav_storetab_kstore_cmx&_encoding=UTF8&slot=desktop-atf-10'
response = requests.get(URL)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
KEY_ID = '' # Your AWS access key ID
SECRET_KEY = '' # Your AWS secret access key



"""Transforming: Cleaning the data"""
# Function finds the data in the specified 'tag' and 'class'
def find_data(tag, attr):
    return soup.find_all(tag, class_=attr)

# Function that converts the data into strings
def find_text(text):
    return str(text.get_text()).strip()

# Function is for removing the unnecessary spaces and newlines from 'div' tags for the author data
def find_author(name):
    return name.replace('by', '').replace(',', ' ,').split(',')[0].replace('\n', '').lstrip().rstrip()

# Holds all the 'div' tags of the comics that will be counted
number_of_comics = [find_text(w) for w in find_data('div', 'csw-grid-list-item-wrapper csw-inline-buy-trigger')]
num = len(number_of_comics)

# Holds the titles for each comic
titles = [find_text(title) for title in find_data('span', 'csw-title-text')]

# Holds the cover arts' image source for each comic
cover_arts = [cover_art['src'] for cover_art in find_data('img', 'csw-item-art')]
# Holds the author for each comic
authors = [find_author(find_text(author)) for author in find_data('div', 'a-row csw-sub-title-row')]

# Holds the required data (currency, dollar, and cent) to develop a price for each comic
prices = []
currency = [find_text(cu) for cu in find_data('span', 'csw-item-price-currency')]
dollars = [find_text(d) for d in find_data('span', 'csw-item-price-dollars')]
cents = [find_text(ct) for ct in find_data('span', 'csw-item-price-cents')]

# Function is for formating the price of a comic correctly with right the currency, dollar, and cent amount
def get_prices(cur, dol, cnt):
    for i in range(num):
        prices.append(f'{cur[i]}{dol[i]}.{cnt[i]}')

get_prices(currency, dollars, cents)

# Holds all the data (Title, Author, Cover Art, and Price) for each comic
new_releases = []

# Function is used to add the data into the 'new_releases' list with the comic's title, author, cover art, and its price
def get_new_releases(t, a, ca, p):
    for i in range(num):
        new_releases.append([t[i], a[i], ca[i], p[i]])

get_new_releases(titles, authors, cover_arts, prices)



"""Loading the data into a predefined bucket called 'comixology-new-releases' in AWS S3"""
header = ['Title', 'Author', 'Cover Art', 'Price']
today = datetime.date.today()
filename = f'/tmp/{today}.csv' # 
bucket = 'comixology-new-releases'

# Retrieving the service source 
s3 = boto3.client('s3',
            region_name='us-east-1',
            aws_access_key_id=KEY_ID,
            aws_secret_access_key=SECRET_KEY)


# Creating a CSV file
with open(f'{filename}', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    # Loading the data into the CSV file that was created
    for i in new_releases:
        writer.writerow(i)

# Closing the CSV file
file.close()

# # Uploading the CSV file to S3
# s3.upload_file(filename, bucket, filename)