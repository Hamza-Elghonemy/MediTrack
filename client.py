import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from login import *
from signup import *
from DoctorGUI import *
import socket 
import numpy as np
from scipy.signal import find_peaks
import json
from PyQt5.QtWidgets import QMessageBox
import uuid # unique id for the users created 
import os
import random
import time
import threading
import base64



HOST = 'localhost'
PORT = 5000
#Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_layout = None
        self.setupUi("signup")
        self.X_Coordinates= []
        self.Y_Coordinates =[]
        self.filteredPatients = []
        self.pointPlotted = 0
        self.current_patient = None
        self.patient_id = 1
        self.timer = QTimer()
        self.timer.setInterval(5000)
        

    def setupUi(self, layout_name):
        if layout_name == "signup":
            self.current_layout = SignUp()
        elif layout_name == "login":
            self.current_layout = LogIn()
        elif layout_name == "Doctor":
            self.current_layout = Ui_MainWindow()

        self.current_layout.setupUi(self)
        if layout_name == "signup":
            self.current_layout.loginButton.clicked.connect(lambda: self.switch_layout("login"))
            self.current_layout.signupButton.clicked.connect(self.register_user)
        elif layout_name == "login":
            self.current_layout.pushButton.clicked.connect(lambda: self.switch_layout("signup"))
            self.current_layout.Login_button.clicked.connect(self.user_login)
        elif layout_name == "Doctor":
            self.current_layout.confirmButton.clicked.connect(self.search_user)
            self.current_layout.searchButton.clicked.connect(self.filter_patients)
            self.current_layout.logoutButton.clicked.connect(self.custom_logout_action)

    def custom_logout_action(self):
        self.timer.stop()
        self.client_socket.close()
        self.switch_layout("signup")
        self.register_user()
        # Add any additional custom logout actions here
        
    def serverFiltration(self):
        try:
            while True:
                self.received = self.client_socket.recv(1024).decode('utf-8')# Receive data from the socket
                print(f"printing the received for filtration : {self.received}")
                self.received = json.loads(self.received)
                self.filteredPatients = self.received
                try:
                    self.current_layout.tableWidget.clearContents()
                    self.current_layout.tableWidget.setRowCount(0)
                    # Add a row to the table
                    # Set data for each cell in the row
                    for patient in self.filteredPatients:
                        row_count = self.current_layout.tableWidget.rowCount()
                        self.current_layout.tableWidget.insertRow(row_count)
                        patient_item = QtWidgets.QTableWidgetItem(patient['username'])
                        vitalSign_item = QtWidgets.QTableWidgetItem(str(patient['vitalSign']))
                        self.current_layout.tableWidget.setItem(row_count, 0, patient_item)     # Set item at column 1
                        self.current_layout.tableWidget.setItem(row_count, 1, vitalSign_item)   # Set item at column 2
                except Exception as e:
                        print(f"error in filteration: {e}")
                break
        except Exception as e:
            print(f"error in receiving data for filtration : {e}")

            
    def filter_patients(self):
        try:
            global HOST, PORT
            self.client_socket.close()
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((HOST, PORT))
            
            currentName= self.current_layout.lineEdit.text()
            filteration = self.current_layout.comboBox.currentText()
            comparedSign = int(self.current_layout.lineEdit_3.text())
            #self.current_patient = search_Patient(currentName)
            update_sign = {
                'checker'  : 1,
                'condition' : filteration,
                'vitalSign' : comparedSign
            }
            
            serialized_data = json.dumps(update_sign)
            self.client_socket.sendall(serialized_data.encode())
            thread = threading.Thread(target=self.serverFiltration)
            thread.start()
            #print(filteration)
            #filteredPatients = filterPatients(filter= filteration ,current_sign= comparedSign)
        #     self.current_layout.tableWidget.clearContents()
        #     self.current_layout.tableWidget.setRowCount(0)
        #     # Add a row to the table
        #     # Set data for each cell in the row
        #     for patient in self.filteredPatients:
        #         patient = json.loads(patient)
        #         row_count = self.current_layout.tableWidget.rowCount()
        #         self.current_layout.tableWidget.insertRow(row_count)
        #         patient_item = QtWidgets.QTableWidgetItem(patient['username'])
        #         vitalSign_item = QtWidgets.QTableWidgetItem(str(patient['vitalSign']))
        #         self.current_layout.tableWidget.setItem(row_count, 0, patient_item)     # Set item at column 1
        #         self.current_layout.tableWidget.setItem(row_count, 1, vitalSign_item)   # Set item at column 2
        except Exception as e:
            print(f"error in filteration: {e}")
            
    def serverRespond(self):
        try:
            while True:
                self.received = self.client_socket.recv(1024).decode('utf-8')# Receive data from the socket
                current = json.loads(self.received)
                if current:
                    print(f"printing the received from search : {current}")
                    self.current_patient = current
                    break
        except Exception as e:
            print(f"error in receiving data for search : {e}")

            
            
    def search_user(self):
        try:
            global HOST, PORT
            self.client_socket.close()
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((HOST, PORT))
            
            currentName= self.current_layout.lineEdit.text()
            #self.current_patient = search_Patient(currentName)
            update_sign = {
                'name' : currentName,
            }
            
            serialized_data = json.dumps(update_sign)
            self.client_socket.sendall(serialized_data.encode())
            print("Data sent successfully")
            thread = threading.Thread(target=self.serverRespond)
            thread.start()
            self.current_layout.nameLabel.setText(self.current_patient['username'])
            self.current_layout.idLabel.setText(f"Age: {self.current_patient['age']}")  
        except Exception as e:
            print(f"error in searching: {e}")
                
    def connect_to_server(self):
        try:
            self.client_socket.connect((self.HOST, self.PORT))
            print("Connected to server")
        except Exception as e:
            print(f"Connection failed: {e}")

    def load_signal_files(self):
        try:
            # List all files in the folder
            files = os.listdir("C://University//Term 2//App Dev//Assignment 4//MediTrack//Datasets//EMG")
            self.signals = []

            # Iterate through each file
            for file_name in files:
                file_path = os.path.join("C://University//Term 2//App Dev//Assignment 4//MediTrack//Datasets//EMG", file_name)
                if os.path.isfile(file_path):
                    # Process the file and extract signal points
                    with open(file_path, 'r') as file:
                        # Assuming each file contains signal points separated by newline characters
                        signal_points = file.read().splitlines()
                        self.signals.append(signal_points)

        except Exception as e:
            print("Error occurred while loading signal files:", e)

    def choose_random_signal(self):
        try:
            # Choose a random signal from the list
            if self.signals:
                random_signal = random.choice(self.signals)
                max_peak = max(random_signal, key=int)
                return max_peak    
            else:
                return 0
        except Exception as e:
            print("Error occurred while choosing a random signal:", e)
            return 0    

    def register_user(self):
        # Create a socket object
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define the server address and port
        self.HOST = 'localhost'
        self.PORT = 5000
                # Connect to the server
        self.client_socket.connect((self.HOST, self.PORT))
        self.timer.timeout.connect(self.simulate)

        username = self.current_layout.textEdit_4.toPlainText()
        self.username = username
        self.email = self.current_layout.textEdit_3.toPlainText()
        current_email = self.email
        age = self.current_layout.ageText.toPlainText()
        gender =None
        if self.current_layout.radioButton_2.isChecked():
            gender = "Male"
        elif self.current_layout.radioButton_3.isChecked():
            gender = "Female"
        password = self.current_layout.textEdit_2.toPlainText()
        confirm = self.current_layout.textEdit.toPlainText()

        # Check if all required fields are filled
        if not all([username, current_email, age, gender, password, confirm]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please fill in all the required fields.")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return
        vitalsign =  []
        sign = random.randint(60, 100)
        vitalsign.append(sign) 
        vitalsign_str = json.dumps(vitalsign)

        self.current_patient = {
            'username': username,
            'email': current_email,
            'age': age,
            'gender': gender,
            'vitalSignList' : vitalsign_str,
            'vitalSign' : sign,
            'password': password
        }
        self.patient_id += 1
        self.Y_Coordinates.append(sign)
        self.X_Coordinates = list(np.arange(len(self.Y_Coordinates)))
        
        # Encode data
        encoded_data = json.dumps(self.current_patient).encode()
        # Send data to server
        client_socket.sendall(encoded_data)
        self.switch_layout("Doctor")
        self.data_line = self.current_layout.graphicsView.plot(self.X_Coordinates[:1], self.Y_Coordinates[:1], pen= "red")
       
    def switch_layout(self, layout_name):
        # Clear existing layout
        #self.current_layout = None
        self.current_layout = layout_name
        self.centralWidget().deleteLater()  # Clear existing widgets
        # Setup new layout
        print(self.current_layout)
        if self.current_layout == "Doctor":
            print(self.current_layout)
            self.timer.start()
        self.setupUi(layout_name)
        self.adjustSize()
        
    def user_login(self):
        username = self.current_layout.username_text.toPlainText()
        password = self.current_layout.password_text.toPlainText()
        
        if not all([username, password]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please fill in all the required fields.")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return
        self.show_current()
        
    def Show_current(self):
        current_sign = self.current_patient['vitalSign']
    
    def simulate(self):
        try:
            vital_sign = random.randint(40, 200)
            if vital_sign < 40:
                self.current_layout.label_5.setPixmap(QtGui.QPixmap("Icons/backwardth.png"))
            elif vital_sign < 70:
                self.current_layout.label_5.setPixmap(QtGui.QPixmap("Icons/rightth.png"))
            elif vital_sign < 90:
                self.current_layout.label_5.setPixmap(QtGui.QPixmap("Icons/leftth.png"))
            else:
                self.current_layout.label_5.setPixmap(QtGui.QPixmap("Icons/forwardth.png"))
            
            #update server
            self.send_data(vital_sign)
            self.current_layout.vitalLabel.setText(str(vital_sign))
            self.current_layout.nameLabel.setText(self.current_patient['username'])
            self.current_layout.idLabel.setText(f"Age: {self.current_patient['age']}")  
            
            self.Y_Coordinates.append(vital_sign)
            self.X_Coordinates = list(np.arange(len(self.Y_Coordinates)))
            self.pointPlotted += 1
            self.current_layout.graphicsView.setLimits(xMin=0, xMax=float('inf'))
            
            self.data_line.setData(self.X_Coordinates[0 : self.pointPlotted + 1], self.Y_Coordinates[0 : self.pointPlotted + 1])  # Update the data.
            self.current_layout.graphicsView.getViewBox().setXRange(max(self.X_Coordinates[0: self.pointPlotted + 1]) - 10, max(self.X_Coordinates[0: self.pointPlotted + 1]))
        except Exception as e:
            print(f"error in simulation:{e}")
            
    #TODO: update using the id   
    def send_data(self, sign):
    # Create a new socket connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        # if self.current_layout.lineEdit.text:
        #     sign = self.current_patient['vitalSign']
        try:
            update_sign = {
                'name' : self.current_patient['username'],
                'vitalSign' : sign  
            }
            
            serialized_data = json.dumps(update_sign)
            self.client_socket.sendall(serialized_data.encode())
            print("Data sent successfully")
            self.client_socket.close()  # Close the connection after sending data
        except Exception as e:
            print(f"Failed to send data: {e}")

            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.load_signal_files()
    #client_program()
    sys.exit(app.exec_())
