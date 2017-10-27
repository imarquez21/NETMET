import socket
import sys

#Defining the variables to create the connection
#Server Address
SERVER_ADDRESS = "127.0.0.1"
PORT = 5236

CONNECT_DATA = ('127.0.0.1', 5236)

#We initialize the messages holding the messages to be sent to the server
MSG = "Hello"

#MSG2 = "Second Message Sent to Server"

#We create the socket by binding the address and port defined.
#socket.SOCK_DGRAM --> For UDP
#socket.SOCK_STREAM --> For TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Establishig TCP Connection
client_socket.connect(CONNECT_DATA)
RCV = "Hello"

while True:
    print "Debug RCV at the beginning of WHILE: ", RCV
    if RCV != "Ciao" or RCV != "ciao":
        MSG = str(raw_input("What is the message to be sent to Server?: "))
        client_socket.sendall(MSG)
        RCV = client_socket.recv(32)
        print "Reply from Server: ", RCV
        print ""
    elif RCV == "Ciao":
        print "Ending script."
        break

'''
#Here we send both messages.
#Sending First Message as UDP
#client_socket.sendto(MSG, (SERVER_ADDRESS,PORT))
#client_socket.sendall(MSG)
#Sending as TCP Message, message 1
#Sending Second Message as UDP
#client_socket.sendto(MSG2, (SERVER_ADDRESS,PORT))
#Sending as TCP Message, message 2
#client_socket.sendall(MSG2)
'''

#Closing the connection
client_socket.close()

#We exit after messages have been sent, end of script
sys.exit()
