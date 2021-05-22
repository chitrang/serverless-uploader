import boto3
import json
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from botocore.config import Config


def upload(bucket,file,object):
    """ uploads a Multipart file for to support large files """
    GB = 1024 ** 3
    config = TransferConfig(multipart_threshold=0.5*GB)

    # Perform the transfer
    s3 = boto3.client('s3')
    print('Uploading %s to Amazon S3 bucket %s' % (file, bucket))
    response = s3.upload_file(Filename=file, Bucket=bucket, Key=object, Config=config)

    print(response)

    # if response.status_code == 200:
    #     print('Upload Successful %s to Amazon S3 bucket %s' % (file, bucket))

    return response


def check(file):
    """ Checks if the file type is correct """
    if file.lower().endswith('.tgz'):
        return True

def list_files(bucket):
    """ list all Files """
    client = boto3.client("s3")
    response = client.list_objects_v2(Bucket=bucket)
    # data = json.loads(response)
    print(response['Contents'])
 
    for i in response['Contents']:
        try:
            response = client.generate_presigned_url('get_object',Params={'Bucket': bucket,'Key': i['Key']}, ExpiresIn=3600)
            print(i['Key'])
            print(response)
        except ClientError as e:
            print(e)

    return response