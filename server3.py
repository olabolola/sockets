import socket
import pickle

HEADER_SIZE = 10

d = {1 : "Hi", 2 : "There!"}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 7777))

s.listen(5)

while True:

	clientsocket, address = s.accept()

	print(f"Received connection from {address}")

	msg = pickle.dumps(d)
	msg = bytes(f"{len(msg)}:<{HEADER_SIZE}", "utf-8") + msg

	clientsocket.send(msg)





