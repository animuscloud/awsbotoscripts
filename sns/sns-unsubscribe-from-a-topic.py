#!/usr/bin/env python
import boto3
import logging

script = 'sns-unsubscribe-from-a-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def unsubscribe(unSubscriptionArn):
      client = boto3.client('sns')
      response = client.unsubscribe(
         SubscriptionArn = unSubscriptionArn
      )
      print unSubscriptionArn


unsubscribe("arn:aws:sns:us-east-1:383762989543:testTopic:a2182d2c-b48f-4680-af1f-625b4f5cddd4")
