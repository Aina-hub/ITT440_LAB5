import socket

#create socket
s = socket.socket()

#choose one port
host_name = socket.gethostname()
IPADDRESS = socket.gethostbyname(host_name)

PORT = 9797

print("Ip address of the server: ", IPADDRESS)
print("Server is listening on port: ", PORT)
print("\nWaiting for connection from a client...")

#bind the port at the server
s.bind(('', PORT))

#server in listening mode
s.listen(10)

while True:
	conn, addr = s.accept()

	msg = "\n\nHi, Client [Ip address: " +addr[0] + "], \nThank you client\n"
	conn.send(msg.encode())

	filename = conn.recv(1024).decode("utf-8")
	file = open(filename, "wb")

	RecvData = conn.recv(99999)

	while RecvData:
		file.write(RecvData)
		RecvData = conn.recv(99999)

#close file once copy is completed
file.close()
print("\nFile is done copied \n")

#close connection
conn.close()
print("Server closed the connection \n")



