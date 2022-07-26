import boto3
from secrets import access_key, secret_access_key
from jupyter_client import client
import json

import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id=access_key,
aws_secret_access_key=secret_access_key
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

result = s3.meta.client.put_object(Body='a=a1+a2, b=b1+b2, c=c1+c2', Bucket='bwaj-task-bucket', Key='task/task.txt')

res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')