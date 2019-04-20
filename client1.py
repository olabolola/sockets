import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#The client socket doesn't want to bind. Instead it wants to connect.
#We give it the port and ip to connect to.

s.connect((socket.gethostname(), 4000))

#Now we want to receive the message from the server.

#Here 8 is our buffer
#You have to determine how many "chunks" of data you want to receive at a time.

while True:
	#Here I want to receive 8 bytes at a time.
	msg = s.recv(8)

	#Recall that message sent from the server was "utf-8"

	print(msg.decode("utf-8"))







