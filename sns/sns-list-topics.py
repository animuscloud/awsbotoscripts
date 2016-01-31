#!/usr/bin/env python
import boto3
import logging

script = 'sns-list-topic.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def listTopics():
    client = boto3.client('sns')
    response = client.list_topics(
       NextToken=''
    )
    print response


listTopics()
