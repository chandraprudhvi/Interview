__author__ = '29146'

import urllib2,os
import paramiko
import time


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.60.35.79',username='root',password='Fusion123')


