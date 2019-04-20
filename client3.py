import socket
import pickle


HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 7777))

while True:

	full_msg = b''
	new_msg = True


	while True:
		msg = s.recv(16)

		if new_msg:
			msglen = int(msg[:HEADER_SIZE])
			new_msg = False

		full_msg += msg.decode("utf-8")

		if len(full_msg) - HEADER_SIZE == msglen:
			print(f"Full message received!!!")
			print(full_msg[HEADER_SIZE:])
			print(full_msg[HEADERSIZE:].decode("utf-8"))
			new_msg = True
			full_msg = b''




