import csv
from http import client
import boto3

with open('credentials.csv','r') as input :
    next(input)
    reader = csv.reader(input)
    for line in reader:

        access_key_id = line [3]
        secret_acces_key = line [4]

photo = 'rahul.jpg'     
client = boto3.client('rekognition',
aws_access_key_id = access_key_id ,
aws_secret_access_key = secret_acces_key )


with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()
    response=client.detect_labels(Image={'Bytes' : source_bytes} , 
    MaxLabels=10)

kms = boto3.client('kms', region_name='us-east-1')    

print (response)    





