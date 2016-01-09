#!/usr/bin/env python
import boto3
import logging

script = 's3-upload-object.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True




def uploadObjectToBucket(bucketName,key,filename):
    s3 = boto3.resource("s3");
    s3.Object(bucketName, key).put(Body=open(filename, 'rb'))





uploadObjectToBucket("animus-test1","test.txt","D:\\temp\\test.txt");