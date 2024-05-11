import socket

def client_program():
    host = 'localhost'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    data = input(' -> ')
    client_socket.send(data.encode())  # send data to the server
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show response

    

if __name__ == '__main__':
    client_program()