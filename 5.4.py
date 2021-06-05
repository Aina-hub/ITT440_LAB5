import socket
import sys

#catch first argument as server ip
if (len(sys.argv) > 1):
	ServerIp = sys.argv[1]
else:
	print("\nRun like \n python3 ClientStore.py < server ip address > \n\n")
	exit(1)

#create socket
s = socket.socket()

#choose one port
PORT = 8888

s.connect((ServerIp, PORT))

filetosend = input('\nEnter the file name to be stored in server:')
s.send(filetosend.encode())
file = open(filetosend, "rb")

SendData = file.read(99999)

while SendData:
	print("\nMessage from server:", s.recv(1024).decode("utf-8"))

	s.send(SendData)
	SendData = file.read(99999)
	print(filetosend + "has been copied to the server\n")

s.close()
