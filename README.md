<!--
title: 'Serverless Uploader'
-->

## Usage

### Deployment
```
$ serverless deploy
```

### Upload

After successful deployment, user can use this script upload.py to upload the file:

```bash
python3 upload.py /Users/cjain/Downloads/100MB.tgz
```
### List all

After successful deployment, user can use this script upload.py to upload the file:

```bash
https://j7z9d2wut0.execute-api.us-east-1.amazonaws.com/dev/list
```

It gives a list of file with key,signed_url. Signed URL can be used to download the file.

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function list
```
