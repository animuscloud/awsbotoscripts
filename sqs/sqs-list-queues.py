#!/usr/bin/env python
import boto3
import logging

script = 'sns-create-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def listQues():
    client = boto3.client('sqs')
    response = client.list_queues(
      QueueNamePrefix=''
    )
    print response


listQues()

