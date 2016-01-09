#!/usr/bin/env python
import boto3
import logging

script = 's3-delete-bucket.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True




def deleteBucket(bucketName):
    s3 = boto3.resource("s3");
    s3.delete_bucket(Bucket=bucketName);





deleteBucket("animus-test1");