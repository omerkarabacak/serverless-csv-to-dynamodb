import boto3
import csv


def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        s3 = boto3.client('s3')
        csvfile = s3.get_object(Bucket=bucket, Key=file_key)
        csvcontent = csvfile['Body'].read().decode('utf-8').splitlines()
        lines = csv.reader(csvcontent)
        headers = next(lines)
        for line in lines:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('csv-table')
            table.put_item(
            Item={
                    'name': line[0],
                    'city': line[1],
                    'country': line[2]
                }
            )