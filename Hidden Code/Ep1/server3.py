import socket
import _thread

password = '47'

serversocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocker.bind(('localhost', 47013))
serversocker.listen(5)


def format(data):
    return str(data).strip()


def client_thread(cs, addr):
    cf = cs.makefile(mode='rw')
    print('Got connection from ' + str(addr))
    has_password = False
    while not has_password:
        print(has_password)
        cf.write('What is the password? ')
        cf.flush()
        data = format(cf.readline())
        print('Client sent: "' + data + '"')
        if data == password:
            cf.write('The password is correct :)\n')
            cf.write('Disconnecting...\n')
            cf.flush()
            clientsocker.shutdown(socket.SHUT_RDWR)
            clientsocker.close()
            has_password = True
        else:
            cf.write('That is not the password :(\n')
            cf.write('Try again\n\n')
            cf.flush()


while True:
    (clientsocker, address) = serversocker.accept()
    _thread.start_new_thread(client_thread, (clientsocker, address))