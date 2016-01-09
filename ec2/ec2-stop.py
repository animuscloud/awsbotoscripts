#!/usr/bin/env python
import boto3
import logging

script = 'ec2-stop.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def  stopInstancesInAccount(owner,Schedule):
    ec2 = boto3.resource('ec2');
    ec2.instances.filter(    Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
             {'Name': 'tag:Owner', 'Values': [owner]}]).stop()



owner = "tojo@animuscloud.com";
schedule = "*";
stopInstancesInAccount(owner,schedule);