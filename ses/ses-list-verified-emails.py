#!/usr/bin/env python
import boto3
import logging

script = 'ses-get-statistics.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def list_verified_emails():
    client = boto3.client("ses")
    response = client.list_verified_email_addresses();
    print response


list_verified_emails()