import os
import sys
import boto3
from secrets import access_key, secret_access_key
from jupyter_client import client

client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

for file in os.listdir():
    if '.txt' in file:
        upload_file_bucket = 'bwaj-task-bucket'
        upload_file_key = 'task/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)

