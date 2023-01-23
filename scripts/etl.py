import requests
from bs4 import BeautifulSoup
import subprocess
import csv
import datetime
import boto3
subprocess.run('clear')

# def lambda_handler():

# Extracting data from Amazon's Comixology page using Beautiful Soup
URL = 'https://www.amazon.com/kindle-dbs/comics-store/home/?ref_=topnav_storetab_kstore_cmx&_encoding=UTF8&slot=desktop-atf-10'
response = requests.get(URL)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
KEY_ID = '' # Your AWS access key ID
SECRET_KEY = '' # Your AWS secret access key


# Transform
new_releases = []

def find_data(tag, attr):
    return soup.find_all(tag, class_=attr)

def find_text(text):
    return str(text.get_text()).strip()

def find_author(name):
    return name.replace('by', '').replace(',', ' ,').split(',')[0].replace('\n', '').lstrip().rstrip()

titles = [find_text(title) for title in find_data('span', 'csw-title-text')]

cover_arts = [cover_art['src'] for cover_art in find_data('img', 'csw-item-art')]

authors = [find_author(find_text(author)) for author in find_data('div', 'a-row csw-sub-title-row')]

prices = []
currency = [find_text(cu) for cu in find_data('span', 'csw-item-price-currency')]
dollars = [find_text(d) for d in find_data('span', 'csw-item-price-dollars')]
cents = [find_text(ct) for ct in find_data('span', 'csw-item-price-cents')]

# Function is for formating the price of a comic correctly with right the currency, dollar, and cent amount
def get_prices(cur, dol, cnt):
    for i in range(len(cur)):
        prices.append(f'{cur[i]}{dol[i]}.{cnt[i]}')

get_prices(currency, dollars, cents)


# Function is used to add the data into the 'new_releases' list with the comic's title, author, cover art, and its price
def get_new_releases(titl, aut, img, pri):
    for i in range(len(titl)):
        new_releases.append([titl[i], aut[i], img[i], pri[i]])

get_new_releases(titles, authors, cover_arts, prices)

# print(new_releases[0])

# Loading the data into a predefined bucket called 'comixology-new-releases' in AWS S3
header = ['Title', 'Author', 'Cover Art', 'Price']
today = datetime.date.today()
filename = f'{today}.csv'
bucket = 'comixology-new-releases'



s3 = boto3.client('s3',
            region_name='us-east-1',
            aws_access_key_id=KEY_ID,
            aws_secret_access_key=SECRET_KEY)


with open(f'{filename}', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in new_releases:
        writer.writerow(i)

file.close()




s3.upload_file(filename, bucket, filename)
    # r = s3.list_objects_v2(Bucket=bucket)
    # print(r['Contents'][0]['Key'])


