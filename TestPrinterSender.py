import socket
from time import sleep
import GlobalConstants
import struct


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10001        # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   
    #this gets a response, but it's an error in the log. Bad bytes!
    #concatMessage = GlobalConstants.StartTransmissionCharacter + "F6" + GlobalConstants.EndTransmissionCharacter

    #This seems to sort of correct- gets "Received SEND_DYNAMIC_DATA_RP1_REMOTE  $6 [24 36 ]" in the log
    concatMessage = GlobalConstants.StartTransmissionCharacter + GlobalConstants.GetSystemStatus + GlobalConstants.EndTransmissionCharacter



    concatMessage = GlobalConstants.StartTransmissionCharacter + "\xf6" + GlobalConstants.EndTransmissionCharacter
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
