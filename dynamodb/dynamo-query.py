#!/usr/bin/env python
import boto3
import logging
from boto3.dynamodb.conditions import Key, Attr

script = 'dynamo-query.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def  queryTable(tablename,uname):
    dynamodb = boto3.resource('dynamodb');
    table = dynamodb.Table(tablename);
    response = table.query(
    KeyConditionExpression=Key('username').eq(uname)
    )
    items = response['Items']
    return items;


items = queryTable('users' ,'mary.homeowner')
print items