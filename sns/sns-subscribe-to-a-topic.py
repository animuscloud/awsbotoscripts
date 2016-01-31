#!/usr/bin/env python
import boto3
import logging

script = 'sns-subscribe-to-a-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def subscribetoToTpic(topicArn,protocol,endPoint):
    client = boto3.client('sns')
    response = client.subscribe(
       TopicArn=topicArn,
       Protocol=protocol,
       Endpoint=endPoint
    )
    print response


subscribetoToTpic("arn:aws:sns:us-east-1:383762989543:testTopic","email","tojo@animuscloud.com")


