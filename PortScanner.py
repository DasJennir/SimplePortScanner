#/bin/bash/python


import sys
import socket
from datetime import datetime
import time
start_time = time.time()

#Variables

user_port = input('What is the range of ports that you would like to scan from (0-65535)? ')

#Define Target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate Host Name to IPv4
else:
    print('Invalid amount of arguments.')
    syntax =  print('Syntax: python3 PortScanner.py <ip>')
    print(syntax)

#Banner

print('-' * 54)
print(f'Scanning Target: {target}')
print(f'Ports: 0-{user_port}')
print('The Scanning has started at ' + str(datetime.now()))
print('-' * 54)

try:
    for port in range(0,int(user_port)):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Return error 
        #print('Scanning port {}'.format(port))
        if result == 0:
            print('Port {} is open'.format(port))
        s.close()
except KeyboardInterrupt:
    print('The Scanning has been stopped')
    print('Turning off...')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved')
    print('Turning off...')
    sys.exit()
except socket.error:
    print('Could not connect to server')
    print('Turning off...')
    sys.exit()

print("--- The code took %s seconds to complete ---" % (time.time() - start_time))