import socket

address = '127.0.0.1'
port = 47011

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((address, port))
socketf = socket.makefile(mode='rw')
socketf.write('Hello, World!\n')
socketf.flush()
print(socketf.readline())