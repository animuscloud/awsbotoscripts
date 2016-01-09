#!/usr/bin/env python

import boto3
import logging

script = 'ec2-create-ebs-ami.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def createAmi(insatnceId):
    client = boto3.client('ec2');
    response = client.create_image(
    DryRun=False,
    InstanceId=insatnceId,
    Name="testAmi",
    Description='This is a test AMI created in Ec2 lab',
    NoReboot=True,
    BlockDeviceMappings=[
        {
            'VirtualName': 'testing',
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'VolumeSize': 10,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2'
            }
        },
    ]
   )

createAmi("i-54a438e5");