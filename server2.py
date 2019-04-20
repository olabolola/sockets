import socket 
import time


#Now we want to make our program more maintainable.
#What if we receive data from server that is more than the buffer size?
#We use headers.
#Server sends message to client saying that: "Hey!!!. I'm about to send you a message that is 50 chars long".
#Client then says: "Ok. I'll wait till I have 50 chars worth of data, then I will know that the message is over".
#After I receive the 50 chars, I will wait for a header again.

#We can have our header have a defined beginning and ending, such as:
#{BEGIN HEADER}
#{END HEADER}

#BUTBUTBUTBUT What happens when people start adding the start and end flags to their message!!!!
#Yeah.

#This is our message.
#Now we want to issue to out message a fixed length header.
#So we put our header, then append to it out msg. So the message is now preceded by our header!!! nice.

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1235))

s.listen(5)


while(True):
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been accepted")

	#This is our message.
	#Now we want to issue to out message a fixed length header.
	#So we put our header, then append to it out msg. So the message is now preceded by our header!!! nice.

	msg = "Welcome to the server"
	msg = f"{len(msg):<{HEADER_SIZE}}" + msg


	clientsocket.send(bytes(msg, "utf-8"))

	while True:
		#pause for 3 seconds
		time.sleep(3)

		msg = f"The time is {time.time()}"
		msg = f"{len(msg):<{HEADER_SIZE}}" + msg

		print(msg)

		clientsocket.send(bytes(msg, "utf-8"))



#Changes on the server side are minimal