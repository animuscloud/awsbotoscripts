#!/usr/bin/env python
import boto3
import logging

script = 'ses-get-statistics.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def getStatistics():
    client = boto3.client("ses")
    response = client.get_send_statistics()
    print response


getStatistics()