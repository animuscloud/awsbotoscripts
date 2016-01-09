#!/usr/bin/env python
import boto.ec2
import logging

script = 'ec2-get-status.py'
version = 'V1'

class ContextFilter(logging.Filter):
  def filter(self,record):
    record.CMDID=script
    return True


def  temrminateOrphanedInstancesInAccount():
    conn = boto.ec2.connect_to_region("us-east-1")
    reservations = conn.get_all_reservations()
    for reservation in  reservations:
        for instance in  reservation.instances:
            if 'Owner' in instance.tags:
                print instance.id + " is owned by " + instance.tags['Owner'];
            else:
                print "Terminating Orphaned instance+ "  + instance.id + " Since it has no owner";
                instance.terminate();
                print instance.id + " is " + instance.state;




temrminateOrphanedInstancesInAccount();