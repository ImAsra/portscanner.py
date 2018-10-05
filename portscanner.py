#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime, time

from socket import socket

subprocess.call('clear', shell=True)

import socket

print('-' * 60)
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)


def item(args):
    pass


print('-' * 60)
print("Please wait, scanning remote host", remoteServerIP)
print('-' * 60)
t1: datetime = datetime.now()


class Errno(object):
    pass


x = int(input("enter starting port: "))
y = int(input("enter ending port: "))
print("searching from port", x, "till port", y)
try:
    for port in range(x, y):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
        sock.settimeout(0.20)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        else:
            result
        print("port {}: closed".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2: datetime = datetime.now()

total = t2 - t1

print('Scanning Completed in:', total, '')
