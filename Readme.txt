Instructions to install and configure prerequisites or dependencies, if any

1. Install python 3
2. Install sqlite

You can download sqlite3 python by going to link
http://www.sqlitetutorial.net/download-install-sqlite/

3.Install psutil package by writing pip install psutil in command prompt
4.Install smtplib package by writing pip install smtplib in command prompt
5. pip install elementtree to install package xml.etree.ElementTree
6. write pip install pypiwin32 in command prompt to install win32evtlogutil # for windows security event logs

I have also included serverConfig.xml file. In this file you can also change the data and values of the clients.

After installing all the necessary packages in command prompt
then run the server.py file by writing command
python server.py 
in command prompt

After running server.py file run the client.py file 
python client.py file


Instructions to create and initialize the database (if required)
In the server.py file I have written code to create database called 'machine.db' and in this database I created a table called 'data'.

# connect to the database
conn = sqlite3.connect('machine.db')

c = conn.cursor()

#We can create the table by uncommenting below lines. So, comment or uncomment the below lines depending upon whether table already exists in database or not
# Create table
c.execute('''CREATE TABLE data
           (DateTime text, IP text, Port text, Username text, Password text, Mail text, totalMemory real, availableMemory real, percent real, usedMemory real, freeMemory real, cpuUsage real, Uptime real)''')



In the server.py file please change the login and password information of gmail.




Assumptions you have made - it is good to explain your thought process and the assumptions you have made
I have made no assumptions. I have created the project according to the requirements.


I have covered all the requirements.

I have faced no issues while completing the assignment.

Constructive feedback for improving the assignment is that the collected and stored data in the database 'machine.db' can be consumed by another application for
useful purposes.



steps to run the scripts and check the data in the database 'machine.db'

1.Open sqlite3.exe
2.Write command
 ATTACH DATABASE 'machine.db' as 'machine';

3. SELECT * FROM data;


 





