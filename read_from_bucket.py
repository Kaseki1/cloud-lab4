import boto3
import pandas as pd
import matplotlib.pyplot as plt

client = boto3.client('s3')
client.download_file('lab4-ipt-kpi-s3-bucket', 'data.csv', '/tmp/data.csv')
csv = pd.read_csv('/tmp/data.csv')

data = dict()
cols = csv['cc'][:57]
vals = csv['rate'][:57]

fig = plt.figure(figsize = (25, 10))

# creating the bar plot
plt.bar(cols, vals)

plt.xlabel('Валюти')
plt.ylabel('Курс відносно гривні')
plt.title('Курс валют до гривні')
plt.savefig('/tmp/figure.png')

client.upload_file('/tmp/figure.png', 'lab4-ipt-kpi-s3-bucket', 'figure.png')