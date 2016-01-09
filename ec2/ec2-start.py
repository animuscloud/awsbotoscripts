#!/usr/bin/env python
import boto3
import logging

script = 'ec2-start.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def  startInstancesInAccount(owner):
    ec2 = boto3.resource('ec2');
    ec2.instances.filter(    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},
             {'Name': 'tag:Owner', 'Values': [owner]}]).start()


owner = "tojo@animuscloud.com"
startInstancesInAccount(owner);