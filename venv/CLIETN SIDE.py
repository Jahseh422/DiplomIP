import socket               # Import socket module

import netifaces
import datetime        #


now = datetime.datetime.now()
a: object = (netifaces.interfaces()) #


#loopback = (netifaces.ifaddresses('{ED29E33C-B605-41DC-A0F5-A6A25C1852C3}')) #
#eth0 = (netifaces.ifaddresses('{93123211-9629-4E04-82F0-EA2E4F221468}')) #




try:
 file = open("out.txt", "a+")                                      #t.
 file.write("================================================\n")  #
 file.write("Date of wirte:\n")
 file.write(str(now.isoformat()))                                  #
 file.write("\n")
 file.write("Infterface list:\n")
 file.write(str(a))
 file.write("\n")
 file.write(" loopback and eth0 :\n")
 file.write("loopback:     ")
 #file.write(str(loopback))                                        #
 file.write("\n")
 file.write("eth0:         ")
 #file.write(str(eth0))                                            #
 file.write("\n================================================")

except FileNotFoundError:                                         #
    print("File not found.")


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
f = open('out.txt','rb')
print ('Sending...')
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
print (s.recv(1024))
s.close                     # Close the socket when done