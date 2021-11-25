import socket
from time import sleep
import GlobalConstants
import struct
from collections import  namedtuple
import pickle
import json
import struct


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10001        # The port used by the server


#this sender works in Read Print mode
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   
    #this gets a response, but it's an error in the log. Bad bytes!
    #concatMessage = GlobalConstants.StartTransmissionCharacter + "F6" + GlobalConstants.EndTransmissionCharacter

    #This seems to sort of correct- gets "Received SEND_DYNAMIC_DATA_RP1_REMOTE  $6 [24 36 ]" in the log
    #concatMessage = GlobalConstants.StartTransmissionCharacter + GlobalConstants.GetSystemStatus + GlobalConstants.EndTransmissionCharacter

    #concatMessage = GlobalConstants.StartTransmissionCharacter + "\xf6" + GlobalConstants.EndTransmissionCharacter
    getPrinterStateRemote = namedtuple("GetPrinterStateRemote", "STX NumberBytesToFollow CheckSum TransmitSequenceNumber MessageID Data ETX")
    #concatMessage = myStruct(GlobalConstants.StartTransmissionCharacter, GlobalConstants.Number4, GlobalConstants.Zero, GlobalConstants.Zero, GlobalConstants.Zero, GlobalConstants.Zero, GlobalConstants.Zero, GlobalConstants.CharacterJ, GlobalConstants.EndTransmissionCharacter)
    #someTuple = getPrinterStateRemote(GlobalConstants.StartTransmissionCharacter, GlobalConstants.Number4, GlobalConstants.Zero, GlobalConstants.Zero, GlobalConstants.Zero, GlobalConstants.CharacterJ, GlobalConstants.EndTransmissionCharacter)
    #concatMessage = pickle.load(someTuple)

    #concatMessage = pickle.dumps(someTuple)  #https://codefather.tech/blog/python-pickle/... we can't use pickle because the other end needs to be python
    #response = json.dumps(someTuple)
    #concatMessage = response.encode('charmap')
    #concatMessage = struct.pack('ccccccccc', "02", "04" "00", "00" "00" "00" "00" "92" "03")
    #concatMessage = "020400000000009203"
    encodedMessage = struct.pack('c', '020400000000009203')

    #encodedMessage = concatMessage.encode('charmap')


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
