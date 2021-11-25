import socket
from time import sleep
import GlobalConstants
import struct


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10001        # The port used by the server


#this sender works in Read Print mode
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   
   #Section 3.4.2 Send Dynamic Data TM3 Remote

    concatMessage = GlobalConstants.StartTransmissionCharacter + "Jones" + GlobalConstants.EndTransmissionCharacter
    #concatMessage =  GlobalConstants.CapitalF + GlobalConstants.CapitalF + GlobalConstants.Number2 + GlobalConstants.PostAmble1

    encodedMessage = concatMessage.encode('charmap')


    s.connect((HOST, PORT))

    while True:
        #data = s.recv(1024)
        #print(data)
        print('sending command...')
        sleep(1)
        s.sendall(encodedMessage)

        #recv = s.recv(1024)

        #print(recv)



#Ignition code:
# import socket
# from time import sleep
# #import GlobalConstants


# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 10002        # The port used by the server


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# print 'waiting...'
# while True:
# 	data = s.recv(1024)
# 	#print data
# 	converted = str(data).decode('charmap')
# 	print converted
#system.util.sendMessage('Edge', 'TcpTest', {'Message':converted})
