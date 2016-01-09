#!/usr/bin/env python
import boto.ec2;
import logging;
import time;

script = 'ec2-launchInstance.py';
version = 'V1';

Name = "Web Server";
Owner = "tojo@animuscloud.com";
Department = "Training";
Company = "Animus Solutions LLC";


class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script;
    return True;


AMI_ID ="ami-60b6c60a";
EC2_KEY_HANDLE = "tj"
INSTANCE_TYPE = "t2.micro"
SECGROUP_HANDLE = "sg-7cff0405"
Schedule = "*"


def createEc2Insatnces(AMI_ID,EC2_KEY_HANDLE,INSTANCE_TYPE,SECGROUP_HANDLE):
    conn = boto.ec2.connect_to_region("us-east-1")
    reservation = conn.run_instances( image_id = AMI_ID,
                                 key_name = EC2_KEY_HANDLE,
                                 instance_type = INSTANCE_TYPE,
                                 security_group_ids = [ SECGROUP_HANDLE ] )
    instance = reservation.instances[0]
    return instance;


def tagTheInsatnce(instance,Name,Owner,Department,Company,Schedule):
    status = instance.update();
    while status == 'pending':
       time.sleep(10);
       status = instance.update();
       print status;
    if status == 'running':
       print "Tagging the instance"
       instance.add_tag("Name",Name)
       instance.add_tag("Owner",Owner)
       instance.add_tag("Department",Department)
       instance.add_tag("Company",Company)
       instance.add_tag("Schedule",Schedule)
    else:
       print('Instance status: ' + status)


instance = createEc2Insatnces(AMI_ID,EC2_KEY_HANDLE,INSTANCE_TYPE,SECGROUP_HANDLE);
tagTheInsatnce(instance,Name,Owner,Department,Company,Schedule)

