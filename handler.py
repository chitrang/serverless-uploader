import json
import sys
import src.service
import src.presigned
from datetime import datetime
bucket="cj-serverless-test"
# file="/Users/cjain/serverless-uploder/serverless-uploader/src/service.py"

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
    print(event)
    now = datetime.now()
    x = now.strftime("%Y-%m-%-%H-%M-%S")

    #name=event['body']['name'].split("/")[-1]
    name=json.loads(event['body'])['name'].split("/")[-1]
    print(name)
    if src.service.check_extension(name):
        response = src.presigned.create_presigned_post(bucket, x+"-"+name)
        # src.service.upload(bucket,event['body'],name)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response),
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
