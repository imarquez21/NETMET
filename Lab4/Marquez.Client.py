import socket

SERVER_ADDRESS = "pl2.tailab.eu"
PORT = 5236
MSG = "Message Sent to Server"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(MSG, (SERVER_ADDRESS,PORT))

