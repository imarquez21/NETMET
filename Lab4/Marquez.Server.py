#Import Socket library as we are working with sockets.
import socket

#Define the varaibles for server IP address and port.
#Later on we will bind this to the socket.
ADDRESS = "127.0.0.1"
PORT = 5236

#We create the socket and make the bind between the IP address and the port.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Creating the bing between the socket, port and IP address defined before.
server_socket.bind((ADDRESS,PORT))

#We run the loop that will keep listening for connections.
while True:
    data, addr = server_socket.recvfrom(1024)
    print "Message: ", data


