import requests
import boto3
import sys

URL = "https://media.gifdb.com/hasbulla-nervous-scared-car-speed-drive-z7p8q1o09beit10r.gif"
FILENAME = "downloaded.gif"
BUCKET_NAME = "ds2002-pqk2va"
EXPIRATION = 604800

http_response = requests.get(URL)
if http_response.status_code == 200:
    with open(FILENAME, "wb") as f:
        f.write(http_response.content)
else:
    sys.exit(1)

s3 = boto3.client('s3')
s3.upload_file(FILENAME, BUCKET_NAME, FILENAME, ExtraArgs={'ACL': 'private'})

url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': BUCKET_NAME, 'Key': FILENAME},
    ExpiresIn=EXPIRATION
)

print(url)
