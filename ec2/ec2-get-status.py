#!/usr/bin/env python
import boto.ec2
import boto3
import logging

script = 'ec2-get-status.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True



def getInstanceStatus(owner):
    ec2 = boto3.resource('ec2');
    instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
             {'Name': 'tag:Owner', 'Values': [owner]}])
    for instance in instances:
            print(instance.id, instance.instance_type)



getInstanceStatus("tojo@animuscloud.com");