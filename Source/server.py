# Modules we need to import
import os
import sqlite3
import socket
import datetime
from xml import etree
import xml.etree.ElementTree as ET
import smtplib




# connect to the database
conn = sqlite3.connect('machine.db')

c = conn.cursor()

#We can create the table by uncommenting below lines
# Create table
#c.execute('''CREATE TABLE data
#           (DateTime text, IP text, Port text, Username text, Password text, Mail text, totalMemory real, availableMemory real, percent real, usedMemory real, freeMemory real, cpuUsage real, Uptime real)''')






#Each client is configured in a server config xml file something like this
#<client ip='127.0.0.1' port='22' username='user' password='password' mail="asa@asda. com"> 
#<alert type="memory" limit="50%" />  
#<alert type="cpu" limit="20%" /> 
#</client>

# We need to parse the 'serverConfig.xml' to get the clients information
tree = ET.parse('serverConfig.xml')
root = tree.getroot()


for child in root:
    # server script should connect to each client 
	ip = child.get('ip')
	port = child.get('port')
	username = child.get('username')
	password = child.get('password')
	mail = child.get('mail')


	HOST = ip
	PORT = int(port)
	
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.bind((HOST, PORT))

	mysock.listen(5)

	(client, (ip, port)) = mysock.accept()


	data = client.recv(2012)

    #After receiving the response from the client script, server script should decode it 
    #and stores it into a relational database along with client ip. 
	data = data.decode()

	data = data.replace('[', '')

	data = data.replace(']', '')

	lis = (data.split(','))


	now = datetime.datetime.now()
	
	# Insert a row of data
	c.execute("INSERT INTO data (DateTime, IP, Port, Username, Password, Mail, totalMemory, availableMemory, percent, usedMemory, freeMemory, cpuUsage, Uptime  ) VALUES ( ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ? )", ( str(now), ip, port, username, password, mail, lis[0], lis[1], lis[2], lis[3], lis[4], lis[5], lis[6] ))



	memoryLimit = ''
	cpuLimit = ''
	for subChild in child:
		if subChild.get('type') == 'memory':
			memoryLimit = subChild.get('limit')

		if subChild.get('type') == 'cpu':
			cpuLimit = subChild.get('limit')

	memoryLimit = float(memoryLimit[0:2])
	cpuLimit = float(cpuLimit[0:2])


    #The server based upon the "alert" configuration of each client sends a mail notification.
	cpuAlert = ''
	memoryAlert = ''

	
	if float(lis[2]) >= memoryLimit :
		memoryAlert = 'You have crossed the memory limit'


	if float(lis[5]) >= cpuLimit :
		cpuAlert = 'You have crossed the cpu limit'


    

    #gmail credentials	please change these credentials
	#in sender we write the mail address of the server. To send the mail you use smtpObj to connect to the SMTP server on the local machine. 	
	sender = 'maheshwarianik@gmail.com'

	# in receivers we write the mail address of the client which are written in the serverConfig.xml file
	password = '1!Mountain'
	
	
	#The server based upon the "alert" configuration of each client sends a mail notification.
	#The notification is sent to the client configured email address using SMTP. 
	#Use a simple text mail format with some detail about the alert. 
	#event logs must be sent via email every time without any condition.
	# mail address of the receiver and message in email 
	TO = mail
	SUBJECT = 'Email from the server'
	TEXT = 'Message from the server : ' + data + "\n   " + cpuAlert + "\n   " + memoryAlert
	
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.ehlo
	smtpObj.login(sender, password)
	
	
	#mail body
	BODY = '\r\n'.join([
	    'To: %s' % TO,
	    'From: %s' % sender,
	    'Subject: %s' % SUBJECT,
	    '',
	    TEXT
	    
	    ])

	

	

	try:
   	  
   	  smtpObj.sendmail(sender, [TO], BODY)         
   	  print ("Successfully sent email")
   	  
	except :
	  
   	  print ("Error: unable to send email")
   	  
        

	mysock.close()
	  





#c.execute("SELECT * FROM data")

#print(c.fetchall())

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()