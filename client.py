import socket
import numpy as np
from scipy.signal import find_peaks

emg_signals = [r'Datasets\EMG\emg_healthy.dat',r'Datasets\EMG\emg_myopathy.dat',r'Datasets\EMG\emg_neuropathy.dat']
emg_data = []
peaks = []
for emg in emg_signals:
    emg_data.append(np.fromfile(emg, dtype=int) / 10000000)
    peaks.append(len(find_peaks(emg_data[-1], height=0)[0]))

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