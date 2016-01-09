#!/usr/bin/env python
import boto3
import logging

script = 'dynamo-delete-item.py'
version = 'V1'


class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True

def deleteItem(table,key1,key2):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    table.delete_item(
      Key={
        'username': key1,
        'last_name': key2
     }
)

deleteItem('users','mary.homeowner','homeowner')
