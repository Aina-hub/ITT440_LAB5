import socket
import os
from _thread import *

ServerSocket=socket.socket()
host=''
port=8889
ThreadCount=0
try:

	ServerSocket.bind((host, port))
except socket.error as e:
	print(str(e))

print('Waiting for a connection...')
ServerSocket.listen(5)

def threaded_client(connection):
	connection.send(str.encode('Welcome to the server \n'))
	while True:
		data=connection.recv(2048)
		reply='Server says:' + data.decode('utf-8')
		print(data)
		if not data:
			break
		connection.sendall(str.encode(reply))
	connection.close()

while True:
	Client,address = ServerSocket.accept()
	print('Connection to:'+address[0]+':'+str(address[1]))
	start_new_thread(threaded_client,(Client,))
	ThreadCount+=1
	print('Thread Number:'+str(ThreadCount))

ServerSocket.close()
