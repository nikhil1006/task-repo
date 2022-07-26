from decimal import Decimal
from io import BytesIO
import os
import sys
import boto3
from secrets import access_key, secret_access_key
from jupyter_client import client
import json

session = boto3.Session()
s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

f = BytesIO()
s3_client.download_fileobj("bwaj-task-bucket", "task/task.txt", f)
print(f.getvalue())