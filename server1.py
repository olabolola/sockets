import socket

#WHAT IS A SOCKET!?!?!?!?
#A socket is an endpoint that sends and receives data
#That endpoint sits at an ip and a port.

#AF_INET corresponds to IPv4. AF = Address family.
#SOCK_STREAM corresponds to TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Now we use s.bind() to bind our socket to an ip and a port.
#socket.gethostname returns the actual naeme
#socket.gethostbyname(socket.gethostname()), gives us the actual ip address

#s.bind() takes a tuple as input.
s.bind((socket.gethostname(), 4000))

#We use s.listen to tell our server to listen for requests. It's a server DUH.
#The parameter '5', means that we will have a queue of 5.

s.listen(5)


#Now keep listening forever
while(True):
	#If we get a connection, store their socket object and their ip address.
	#ip address and port number of client are stored in address
	clientsocket, address = s.accept()

	print(f"connection from {address} has been established!")


	#Now we want to send information to client
	#You can send bytes(), or just type in a string then .encode it.
	#The second parameter determines what type of bytes we are sending.
	clientsocket.send(bytes("Welcome to the server", "utf-8"))









