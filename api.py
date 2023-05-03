import requests
import pandas as pd
import boto3
import matplotlib.pyplot as plt

response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json') # Note: the timeout parameter is very useful for requests!
data = response.content.decode()
df = pd.read_json(data)
df.to_csv('data.csv', index=False)

# upload file to bucket
client = boto3.client('s3')
client.create_bucket(Bucket='lab', location='ap-northeast-1', CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'})
client.upload_file('data.csv', 'lab', 'data.csv', location='ap-northeast-1')


