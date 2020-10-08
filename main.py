#!/usr/bin/python

# Code Version #
software = "v.0.0.0"

import os,subprocess
from serial import Serial
import time, datetime
import pytz

GatewayMessage ='HTTP/1.1 401 Unauthorized'
internetMessage = 'HTTP/1.1 200 OK'

my_date = str(datetime.datetime.now(pytz.timezone('Pacific/Honolulu')))
filename = my_date[0:len('2020-10-07 19:56:37')]+".log"
f= open("{}".format(filename),"w+")

while True:
    print('checking first gate')
    internetCheck = subprocess.check_output('curl -IsS http://www.google.com | head -n 1', shell=True)
    print('first gate complete')
    gatewayCheck = subprocess.check_output('curl -IsS http://192.168.200.1 | head -n 1', shell=True)
    
    my_date = datetime.datetime.now(pytz.timezone('Pacific/Honolulu'))
    if(internetCheck[0:len(internetMessage)] == internetMessage):
        f = open("/home/pi/connectionProbe/{}".format(filename), "a")
        f.write('internet is up at {}\n'.format(my_date))
        f.close()
	print('internet up at {}'.format(my_date))
    else:
        f = open("/home/pi/connectionProbe/{}".format(filename), "a")
        f.write('internet is ---DOWN--- at {}\n'.format(my_date))
        f.close()
	print('internet down at {}'.format(my_date)) 
    if(gatewayCheck[0:len(GatewayMessage)] == GatewayMessage):
        f = open("/home/pi/connectionProbe/{}".format(filename), "a")
        f.write('gateway is up at {}\n'.format(my_date))
        f.close()
	print('gateway up at {}'.format(my_date))
    else:
        f = open("/home/pi/connectionProbe/{}".format(filename), "a")
        f.write('gateway is  ---DOWN--- at {}\n'.format(my_date))
        f.close()
	print('gateway down at {}'.format(my_date))




    time.sleep(120)
