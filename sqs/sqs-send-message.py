#!/usr/bin/env python
import boto3
import logging
import json

script = 'sqs-sens-message.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def  sendMessage(queue,message):
     client = boto3.client('sqs')
     response = client.send_message(
     QueueUrl= queue,
     MessageBody= message,
     DelaySeconds=1
     )
     print response




sendMessage("https://queue.amazonaws.com/383762989543/test13","this is a test message")
