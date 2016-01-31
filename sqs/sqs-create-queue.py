#!/usr/bin/env python
import boto3
import logging

script = 'sns-create-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def createQueue(queueName):
    client = boto3.client('sqs')
    response = client.create_queue(
    QueueName= queueName ,
    Attributes={
        "VisibilityTimeout" : "60"
    }
    )
    print response


createQueue("animus-test-queue")

