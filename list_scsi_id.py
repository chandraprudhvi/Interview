__author__ = '29146'

import paramiko
import time
import os
import re


alias = 'alias scsi_new1 () { cd "'"/dev/disk/by-id/"'" && ls | grep scsi; }'
pattern = re.compile(alias)

homefolder = os.path.expanduser('~')
bashrc = os.path.abspath('%s~/.bashrc')
print bashrc

def appendToBashrc():
  with open(bashrc, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if pattern.match(line):
        return
    out = open(bashrc, 'a')
    out.write('\n%s' % alias)
    out.close()

def scsi_id():
 ipaddress = '10.60.34.81'
 userid = 'root'
 password = 'Fusion123'
 print 'connecting to .......' + ' ' + ipaddress
 print str(userid)
 print str(password)

 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

 ssh.connect(ipaddress,username=userid,password=password)

 #command = "alias scsi_new1 () { cd "'"/dev/disk/by-id/"'" && ls | grep scsi; }"
 #command="hostname"
 #stdin, stdout, stderr = ssh.exec_command(command)
 #sshdata = stdout.readlines()
 stdin,stdout,sderr = ssh.exec_command("scsi >> /tmp/stupid_detils.txt")

 #print sshdata
 #print command
 #print stdout.read()




if __name__ == '__main__':
 appendToBashrc()
 scsi_id()