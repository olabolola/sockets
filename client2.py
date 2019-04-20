import socket

#Now we want the same headersize from server

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1235))

while True:
	
	#Variable to store full message
	full_msg = ''

	#variable to indicate whether a header is coming or just raw data
	new_msg = True


	while True:
		#Here we just receive anything as long as it is greater than the HEADER_SIZE.
		#We just slice out the rest later.
		msg = s.recv(16)

		#if it is a new message we want to receive the header.
		if new_msg:
			#Now get the header.
			print("new message len:", msg[:HEADER_SIZE])
			#Oh the magic of python. We can convert it to int even though there are a bunch of chars in it.
			msglen = int(msg[:HEADER_SIZE])
			print(msglen)

			new_msg = False

		print(f'The full msg length is {msglen}')

		#Here we want to keep on adding 16 bytes at a time to out full msg.s
		full_msg += msg.decode("utf-8")

		#Just for debugging
		print(len(full_msg))

		#Check if we have received the full message each time.
		if(len(full_msg) - HEADER_SIZE == msglen):
			print("Full message received!!!!!")

			#Print everything except for the header
			print(full_msg[HEADER_SIZE:])

			#After we have received the full message, we are now ready to reeive another one.
			new_msg = True

			#Also, we need to reset the message.
			full_msg = ''

	print(full_msg)







