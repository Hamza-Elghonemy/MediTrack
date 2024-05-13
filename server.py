import redis
import json
import socket
import numpy as np
 

redis_host='redis-17832.c281.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 17832
password = "Hamza123"
r = redis.Redis(redis_host,redis_port, db=0, password=password)
  
class servers(): 
    def __init__(self):
        self.patient_id = 0 
    def store_patients(self,patients):
        # Generate a unique key for the patient data
        self.patient_id = r.incr('patient_id_counter')
        # Store the JSON data in a hash
        r.hmset(f'patient:{patients['username']}', patients)
        print(f"Patient data stored with ID: {self.patient_id}")
        return self.patient_id
        
    def update_diagnosis(self, name, vitalsign):
        patientList = self.get_patients_and_doctors()
        _,patient = self.find_patient(name, patientList)
        # Check if the patient exists
        if r.exists(f'patient:{patient['username']}'):
            # Update the diagnosis in the hash
            r.hset(f'patient:{patient['username']}', 'vitalSign', vitalsign)
            print(f"Diagnosis updated for patient with ID: {self.patient_id}")
        else:
            print(f"Patient with ID {self.patient_id} doesn't exist")
            
    def find_patient(self,name, patients,password = None):
        for patient in patients:
            if patient['username'] == name or patient['password'] == password:
                return self.patient_id, patient
        return None
    
    def filterPatients(self, patients, sign, filtration):
        matching_patients = []
        for patient in patients:
                if filtration == "Equal to" and int(patient['vitalSign']) == sign:
                    print(f"current patient: {patient['username']}")
                    matching_patients.append(patient)
                elif filtration == "Greater than" and int(patient['vitalSign']) > sign:
                    print(f"current patient: {patient['username']}")
                    matching_patients.append(patient)
                elif filtration == "Less than" and int(patient['vitalSign']) < sign:
                    print(f"current patient: {patient['username']}")
                    matching_patients.append(patient)
        return matching_patients

    def get_patients_and_doctors(self):
        patients = []

        # Retrieve patients
        patient_keys = r.keys("patient:*")
        for key in patient_keys:
            patient_data = r.hgetall(key)
            patients.append({k.decode(): v.decode() for k, v in patient_data.items()})
        return patients

        
    def server_program(self):
        host = 'localhost'
        port = 5000  # initiate port number above 1024

        server_socket = socket.socket()  # get instance
        server_socket.bind((host, port))  # bind host address and port together
        
        while True:
            server_socket.listen(1)
            conn,_ = server_socket.accept()  # accept new connection 
            data = conn.recv(1024).decode()
            if data:
                user_data = json.loads(data)
                if len(user_data) >2:
                    self.patient_id = self.store_patients(user_data)
                elif len(user_data) == 2:
                        currentName = user_data['name']
                        vitalsign = user_data['vitalSign']
                        self.update_diagnosis(currentName, vitalsign)
                # elif len(user_data) ==2:
                #     patient_lists = self.get_patients_and_doctors()
                #     name = user_data['username']
                #     current_patient = self.find_patient_by_name(name, patient_lists)
                #     if current_patient:
                #         returned_data = json.dumps(current_patient)
                #         conn.sendall(returned_data.encode())
                #     else: 
                #         conn.sendall("false".encode())
                #     continue
                    
            server_data = "recieved"
            conn.send(server_data.encode())  # send data to the client
        
if __name__ == '__main__':
    s = servers()
    s.server_program()

