#!/usr/bin/env python
import boto3
import logging

script = 'dynamodb-update-item.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True

class User(object):
    username = ""
    first_name = ""
    last_name = ""
    age = ""
    account_type = ""


def getItem(table,key1,key2):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    response = table.get_item(
      Key={
        'username': key1,
        'last_name': key2
      }
    )
    item = response['Item']
    return item;


def updateItem(table,key1,key2,age):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    response = table.get_item(
      Key={
        'username': key1,
        'last_name': key2
      }
    )
    item = response['Item']
    item['age'] = age;
    table.put_item(Item=item);



user = getItem('users','bob.smith','smith');
print    user['age'];
updateItem('users','bob.smith','smith',26);
user = getItem('users','bob.smith','smith');
print    user['age'];

