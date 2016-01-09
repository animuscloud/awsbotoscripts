#!/usr/bin/env python
import boto3
import logging
from boto3.dynamodb.conditions import Key, Attr

script = 'dynamo-scan.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def scanTable(tablename,age):
    dynamodb = boto3.resource('dynamodb');
    table = dynamodb.Table(tablename);
    response = table.scan(
    FilterExpression = Attr('age').gt(age)
    )
    items = response['Items']
    return items;


items = scanTable('users' ,26)
print items