#!/usr/bin/env python
import boto3
import logging

script = 's3-bucket-keys-list.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True




def listBucketAndKeys():
    s3 = boto3.resource("s3");
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print(key.key)



listBucketAndKeys();