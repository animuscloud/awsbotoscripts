#!/usr/bin/env python
import boto3
import logging

script = 'ses-sendEmail.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def  sendEmail(source,to,message):
    client = boto3.client("ses")
    response = client.send_email(
    Source= source,
    Destination={
        'ToAddresses': [
            to,
        ]
    },
    Message={
        'Subject': {
            'Data': 'test email',
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': message,
                'Charset': 'UTF-8'
            }
        }
    }
    )
    print response


sendEmail("tojopjose@gmail.com","tojo@animuscloud.com","this is a test email")


