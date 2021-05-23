import json
import sys
import src.service

bucket="cj-serverless-test"
# file="/Users/cjain/serverless-uploder/serverless-uploader/src/service.py"

def hello(event, context):
    body = {
        "message": "Serveless Test",
        "input": event,
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
        'body': body,
        "isBase64Encoded": False
    }

def upload(event, context):
    if src.service.check_extension(event):
        name=event.split("/")[-1]
        src.service.upload(bucket,event,name)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': name,
            "isBase64Encoded": False
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': "Not Correct File Type. Expecting only .tgz",
            "isBase64Encoded": False
        }