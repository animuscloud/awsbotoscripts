#!/usr/bin/env python
import boto3
import logging

script = 'sns-delete-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def deleteTopic(topicArn):
    client = boto3.client('sns')
    response = client.delete_topic(
      TopicArn = topicArn
    )
    print response


deleteTopic("arn:aws:sns:us-east-1:383762989543:testTopic")
