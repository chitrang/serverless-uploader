import json
import sys
import src.service

bucket="cj-serverless-test"
# file="/Users/cjain/serverless-uploder/serverless-uploader/src/service.py"

def hello(event, context):
    body = {
        "message": "Serveless Test"
    }
    print(event)
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def list(event, context):    
    body = src.service.list_files(bucket)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body),
        "isBase64Encoded": False
    }

def upload(event, context):
    if src.service.check_extension(event['body']):
        name=event['body'].split("/")[-1]
        src.service.upload(bucket,event['body'],name)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({"Filename": name}),
            "isBase64Encoded": False
        }
    else:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({"message": "Not Correct File Type. Expecting only .tgz"}),
            "isBase64Encoded": False
        }