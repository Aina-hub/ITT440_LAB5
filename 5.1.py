import socket

s = socket.socket()

port = 8888

s.connect(('192.168.56.102',port))

data = s.recv(1024)

s.send(b'Hai saya client.Terima kasih!')

print(data)

s.close()

