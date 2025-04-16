#!/bin/bash

LOCAL_FILE="$1"
BUCKET_NAME="$2"
EXPIRATION="$3"

FILENAME=$(basename "$LOCAL_FILE")

aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/$FILENAME"

aws s3 presign "s3://$BUCKET_NAME/$FILENAME" --expires-in "$EXPIRATION"
