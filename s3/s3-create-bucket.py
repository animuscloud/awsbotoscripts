#!/usr/bin/env python
import boto3
import logging

script = 's3-create-bucket.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True




def createBucket(bucketName):
    s3 = boto3.resource("s3");
    s3.create_bucket(Bucket=bucketName);




createBucket("animus-test1");