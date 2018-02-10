import socket
import _thread

password = '47'

serversocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocker.bind(('localhost', 47012))
serversocker.listen(5)


def format(data):
    return str(data).strip()


def client_thread(cs, addr):
    cf = cs.makefile(mode='rw')
    print('Got connection from ' + str(addr))
    cf.write('What is the password? ')
    cf.flush()
    data = format(cf.readline())
    print('Client sent: "' + data + '"')
    if data == password:
        cf.write('\nThe password is correct :)')
    else:
        cf.write('\nThat is not the password :(')
    cf.flush()
    clientsocker.shutdown(socket.SHUT_RDWR)
    clientsocker.close()


while True:
    (clientsocker, address) = serversocker.accept()
    _thread.start_new_thread(client_thread, (clientsocker, address))