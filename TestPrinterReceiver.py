import socket
from time import sleep
#import GlobalConstants


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10002        # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #testJson = '{"sequenceNumber":"2", "timestamp": "2020-09-21T23:04:59", "messageName": "KEEP_ALIVE", "correlationId": "ded5a3f3-aaf2-4ea7-a6e0-b27ca20274f0", "status": "ACK" }'
    #testDVTCF = '{"sequenceNumber":"2", "timestamp": "2020-09-21T23:04:59", "messageName": "DVTCF", "correlationId": "473d41b6-f914-4f80-906d-1fe41250e598", "status": "ACK" }'
    #testJson = getSortMessageJson()
    #concatMessage = GlobalConstants.StartTransmissionCharacter + "\x31" + GlobalConstants.EndTransmissionCharacter
    #encodedMessage = concatMessage.encode('ascii')

    s.connect((HOST, PORT))
    print('waiting....')
    while True:
        #data = s.recv(1024)
        #print(data)
        #sleep(3)
        #s.sendall(encodedMessage)

        recv = s.recv(1024)

        print(recv)