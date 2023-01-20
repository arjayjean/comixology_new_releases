import transform as t
import csv
import datetime
import boto3
# import pandas as pd

header = ['Title', 'Author', 'Image', 'Price']
data = t.new_releases
today = datetime.date.today()
filename = f'{today}.csv'
bucket_name = 'comixology-new-releases'

KEY_ID = '' # Your AWS access key ID
SECRET_KEY = '' # Your AWS secret access key

s3 = boto3.client('s3',
            region_name='us-east-1',
            aws_access_key_id=KEY_ID,
            aws_secret_access_key=SECRET_KEY)

def load():
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in data:
            writer.writerow(i)

    file.close()

load()

s3.upload_file(filename, bucket_name, filename)
r = s3.list_objects_v2(Bucket=bucket_name)


print(r['Contents'][0]['Key'])