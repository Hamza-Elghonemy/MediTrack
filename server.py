import socket
import redis

def server_program():
    host = 'localhost'
    port = 5000  # initiate port number above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # Create a Redis connection
    r = redis.Redis(host='redis-17832.c281.us-east-1-2.ec2.redns.redis-cloud.com', port=17832, db=0,password='Hamza123')

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))

        # Store the data in Redis
        r.set('client_data', data)

        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
        

    

if __name__ == '__main__':
    server_program()