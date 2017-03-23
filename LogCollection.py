__author__ = '29146'

import sys
import paramiko
import time
import datetime
import socket
import socket
import fcntl
import struct

# def get_ip_address(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])

 # '192.168.0.110'




def collect_logs():
 # ipaddress = raw_input("Enter ipaddress of machine to collect logs: ")
 # userid = raw_input("Enter login userid@"+ipaddress+": ")
 # password = raw_input("Enter login password@"+ipaddress+": ")

 ipaddress = '10.60.34.81'
 userid = 'root'
 password = 'Fusion123'
 timestr = time.strftime("%Y%m%d-%H%M%S")
 logfilename = 'initiator_log_'+ipaddress + '_' + timestr + '.tar.gz'
 print 'connecting to .......' + ' ' + ipaddress
 print str(userid)
 print str(password)

 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

 ssh.connect(ipaddress,username=userid,password=password)
 # stdin,stdout,sderr = ssh.exec_command("lsscsi >> /tmp/lsscsi.txt")
 # print "tar -zcv" + ' ' + '/var/log' + ' '+ '/etc/multipath.conf'+ ' ' + '/tmp/lsscsi.txt'+ ' ' + '>' + ' ' + '/tmp/' + logfilename
 #
 # stdin,stdout,stderr = ssh.exec_command("tar -zcv" + ' ' + '/var/log' + ' '+ '/etc/multipath.conf'+ ' ' + '/tmp/lsscsi.txt'+ ' ' + '>' + ' ' + '/tmp/' + logfilename)
 # print stderr.read()
 stdin,stdout,sderr = ssh.exec_command("cat /etc/redhat-release")
 #stdin,stdout,sderr = ssh.exec_command("uname -a >> /tmp/os_details.txt")

 operating_system = stdout.read()
 print operating_system








 #commnd1 = "tar -zcv" + ' ' + '/var/log' + ' '+ '/etc/multipath.conf' + ' ' + '>' + ' ' + '/tmp/' + logfilename


 #print commnd1
 #print logfilename
 #print operating_system



 #
 # x = socket.gethostbyname()
 # print x






if __name__ == '__main__':
    collect_logs()