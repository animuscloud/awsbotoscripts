#!/usr/bin/env python
import boto3
import logging

script = 'sns-publish.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def   publishToATopic(topicArn,message):
      client = boto3.client('sns')
      response = client.publish(
        TopicArn= topicArn,
        Message=message,
        Subject="test"
      )
      print response


publishToATopic("arn:aws:sns:us-east-1:383762989543:testTopic","this is a test message")