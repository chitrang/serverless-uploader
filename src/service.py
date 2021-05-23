import boto3
import json
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from botocore.config import Config
import src.presigned

# def upload(bucket,file,object):
#     """ uploads a Multipart file for to support large files """
#     GB = 1024 ** 3
#     config = TransferConfig(multipart_threshold=0.5*GB)

#     #s3 = boto3.client('s3')
#     s3 = boto3.resource('s3')
#     print('Uploading %s to Amazon S3 bucket %s as %s' % (file, bucket,object))
#     response = s3.meta.client(Filename=file, Bucket=bucket, Key=object, Config=config)

#     print(response)
#     return response

def check_extension(file):
    """ Checks if the file type is correct """
    if file.lower().endswith('.tgz'):
        print("File %s has correct extension" % file)
        return True
    else:
        print("File %s has incorrect extension" % file)
        return False

def list_files(bucket):
    """ list all Files """
    client = boto3.client("s3")
    response = client.list_objects_v2(Bucket=bucket)
    # data = json.loads(response)
    url_list=[]
    print(response['Contents'])
 
    for i in response['Contents']:
        try:
            print("Generating url for %s", i['Key'])
            url_list.append({i['Key']: client.generate_presigned_url('get_object',Params={'Bucket': bucket,'Key': i['Key']}, ExpiresIn=7200)})
        except ClientError as e:
            print(e)
    print(url_list)
    return url_list