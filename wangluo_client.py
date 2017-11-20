#!/usr/bin/python3
#  -*- coding: utf-8 -*-
import socket
import sys

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message: '
          + msg[1])
    sys.exit()
else:
    print('Socket Created')

host = 'www.baidu.com'
port = 80
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
else:
    s.connect((remote_ip, port))
    print('Socket Connected to ' + host + ' on ip ' + remote_ip)

message = "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message)
except socket.error:
    print('Send failed')
    sys.exit()
else:
    print('Message send successfully')

reply = s.recv(4096)
print(reply)

s.close()