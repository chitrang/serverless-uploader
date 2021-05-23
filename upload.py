import requests
import os
import sys
import json

file = sys.argv[1]
print(file)
if os.path.exists(file):
    print("File exists %s" % os.path.basename(file))
file_size = os.stat(file).st_size
print("File_Size: ", file_size)


url = "https://j7z9d2wut0.execute-api.us-east-1.amazonaws.com/dev/upload"
body = {'name': file}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(body), headers=headers)

if r.status_code == 200:
    response = json.loads(r.content)
    print(response)
    with open(file, 'rb') as f:
        files = {'file': (file, f)}
        http_response = requests.post(response['url'], data=response['fields'], files=files)
else:
    print("status Code %d" % r.status_code, r.content)
    print("Upload request Failed") 
