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


def receiveMessage(queueUrl):
    client = boto3.client('sqs')
    response = client.receive_message(
    QueueUrl=queueUrl,
    )
    print response;


receiveMessage("https://queue.amazonaws.com/383762989543/test13")