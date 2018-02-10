import socket
import _thread

serversocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocker.bind(('localhost', 47011))
serversocker.listen(5)


def format(data):
    return str(data).strip()


def client_thread(cs, addr):
    cf = cs.makefile(mode='rw')
    print('Got connection from ' + str(addr))
    data = format(cf.readline())
    print('Client sent: "' + data + '"')
    cf.write(data)
    cf.flush()
    clientsocker.shutdown(socket.SHUT_RDWR)
    clientsocker.close()
    print('Connection closed')



while True:
    (clientsocker, address) = serversocker.accept()
    _thread.start_new_thread(client_thread, (clientsocker, address))