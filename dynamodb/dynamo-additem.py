#!/usr/bin/env python
import boto3
import logging

script = 's3-create-table.py'
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


def makeUser(username,firstname,lastname,age,accounttype):
    user =  User();
    user.username = username;
    user.firstname = firstname;
    user.lastname = lastname;
    user.age = age;
    user.accounttype = accounttype;
    return user

def addUserToUserTable(user):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    table.put_item(
       Item={
            'username': user.username,
            'first_name': user.firstname,
            'last_name': user.lastname,
            'age': user.age,
            'account_type': user.accounttype,
       }
    )

userOne = makeUser("bob.smith","bob","smith",34,"checking");
userTwo = makeUser("mary.homeowner","mary","homeowner",44,"checking");
userThree = makeUser("brady.smith","brady","smith",37,"Savings");

addUserToUserTable(userOne)
addUserToUserTable(userTwo)
addUserToUserTable(userThree)