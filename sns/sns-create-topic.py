#!/usr/bin/env python
import boto3
import logging

script = 'sns-create-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def  createSnsTopic(topicName):
    client = boto3.client('sns')
    response = client.create_topic(
      Name=topicName
    )
    print response


createSnsTopic("testTopic")