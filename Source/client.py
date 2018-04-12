#modules we need to import
from __future__ import print_function
import psutil
import time
import socket
import win32evtlog
import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlogutil # for windows security event logs
import winerror



# method which returns uptime
def uptime1():
    return time.time() - psutil.boot_time()
    
    
    

cpuUsage = psutil.cpu_percent()

memUsage = list(psutil.virtual_memory()) #  physical memory usage


totalMemory = memUsage[0]
availableMemory = memUsage[1]
percent = memUsage[2]
usedMemory = memUsage[3]
freeMemory = memUsage[4]

uptime = uptime1()


# we find windows security event logs from here
server = 'localhost' # name of the target computer to get event logs
logtype = 'System'
hand = win32evtlog.OpenEventLog(server,logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

events = win32evtlog.ReadEventLog(hand, flags,0)
events_list = [event for event in events]

# convert the windows security event logs to a well formatted string
data_security_events = ''

for i in events_list:
     data_security_events = data_security_events + 'Event category is ' + str(i.EventCategory) + ', Event source name is ' +   str(i.SourceName) + ', data is ' + str( i.StringInserts) + '.  '

#close the event log
win32evtlog.CloseEventLog(hand)




# we are sending memUsage, cpuUsage, uptime, data_security_events in the form of list to the server
lis = [ memUsage, cpuUsage, uptime, data_security_events]

#address of the server
HOST = 'localhost'  # You can change the address of server from localhost to other server address
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))

#convert list to string to send the data
l = str(lis)

# we are sending memUsage, cpuUsage, uptime, data_security_events in the form of list to the server
#  encrypt the data before sending it to server.
mysock.send(l.encode())
