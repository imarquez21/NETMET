# Import Socket library as we are working with sockets.
import socket
import time
import sys

# Define the variables for server IP address and port.
# Later on we will bind this to the socket.
ADDRESS = ""
PORT = 5236

# Variables to keep track of time
start_time = None
end_time = None
time_difference = None

# Identify when we have received two packages
messages_counter = 0

# We create the socket and make the bind between the IP address and the port.
# socket.SOCK_DGRAM --> For UDP
# socket.SOCK_STREAM --> For TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creating the bind between the socket, port and IP address defined before.
server_socket.bind(('', PORT))

# Listening on the TCP socket we have created
server_socket.listen(1)

print "Waiting for connection..."

# We run the loop that will keep listening for connections.
connection, client_address = server_socket.accept()
print "Connection established with: ", client_address

while True:
    print "Anything to say?"
    data1_tcp = connection.recv(32)
    print "Message received from Client: ", data1_tcp
    print ""
    if data1_tcp == "Hello":
        connection.sendall("Hi back, try harder.")
        print("Waiting for next attempt.")
    elif data1_tcp == "power-off":
        connection.sendall("Nice try, but not there yet")
        print("Waiting for next attempt.")
    elif data1_tcp == "reboot":
        connection.sendall("Almost there, very close")
        print("Waiting for next attempt.")
    elif data1_tcp == "shutdown" or data1_tcp == "Shutdown":
        connection.sendall("Got it, shutting down.")
    elif data1_tcp == "Ciao" or data1_tcp == "ciao":
        connection.sendall("Ciao")
        print "Shutting down..."
        break
    else:
        connection.sendall("Not even close.")

print "Good bye."
connection.close()

'''
#First Message received
#data1, addr = server_socket.recvfrom(1024)
#print "Message 1: ", data1
#start_time = time.time()
# messages_counter+=1
#Second Message received
#data2, addr = server_socket.recvfrom(1024)
#print "Message 2", data2
data2_tcp = connection.recv(32)
print "Message 2 as TCP: ", data2_tcp
end_time = time.time()
messages_counter+=1
data_received_size = int(round((len(data1_tcp+data2_tcp)*8)))
if messages_counter == 2:
    time_difference = end_time - start_time
    print "Time difference between two packets is: ", time_difference, "seconds"
    print "Bandwidth is: ", data_received_size/time_difference, "Bits/s"
    connection.close()
    break
'''

sys.exit()
