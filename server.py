import redis
import json
import socket
import numpy as np
import base64

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
        patient = self.find_patient(name, patientList)
        # Check if the patient exists
        if r.exists(f'patient:{patient["username"]}'):
            current_vitalsign_str = r.hget(f"patient:{patient['username']}", "vitalSignList")

            # Check if the string is not empty
            if current_vitalsign_str:
                # Load the JSON string to a list
                current_vitalsign = json.loads(current_vitalsign_str)

                # Append the new vitalsign to the list
                current_vitalsign.append(vitalsign)

                # Convert the updated list to a JSON string
                updated_vitalsign_str = json.dumps(current_vitalsign)

                # Update the vitalSignList in the hash
                r.hset(f'patient:{patient["username"]}', 'vitalSignList', updated_vitalsign_str)
                r.hset(f'patient:{patient["username"]}', 'vitalSign', vitalsign)
                print(f"Diagnosis updated for patient with ID: {self.patient_id}")
            else:
                print(f"No existing vitalSignList for patient with ID: {self.patient_id}")
        else:
            print(f"Patient with ID {self.patient_id} doesn't exist")
            
    def find_patient(self,name, patients,password = None):
        for patient in patients:
            if patient['username'] == name or patient['password'] == password:
                return patient
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
                try:
                    user_data = json.loads(data)
                except json.JSONDecodeError:
                    print("Received invalid JSON data:", data)
                    continue
                if  len(user_data) ==1:
                    patient_lists = self.get_patients_and_doctors()
                    name = user_data['name']
                    current_patient = self.find_patient(name, patient_lists)
                    if current_patient:
                        returned_data = json.dumps(current_patient)
                        conn.send(returned_data.encode())
                    else: 
                        conn.send("false".encode())
                    continue
                elif len(user_data) == 3 :
                    patient_lists = self.get_patients_and_doctors()
                    current_filtration = user_data['condition']
                    currentsign =user_data['vitalSign']
                    current_list = self.filterPatients(patients=patient_lists, sign=currentsign,filtration= current_filtration)
                    current = json.dumps(current_list)
                    conn.send(current.encode())
                
                elif len(user_data) == 2 :
                        currentName = user_data['name']
                        vitalsign = user_data['vitalSign']
                        self.update_diagnosis(currentName, vitalsign)
                        server_data = "recieved"
                        conn.send(server_data.encode())  # send data to the client
                elif  len(user_data) >4:
                    self.patient_id = self.store_patients(user_data)
                    server_data = "recieved"
                    conn.send(server_data.encode())  # send data to the client
                    
            
        
if __name__ == '__main__':
    s = servers()
    s.server_program()

# def get_patients_and_doctors():
#     patients = []
#     doctors = []

#     # Retrieve patients
#     patient_keys = r.keys("patient:*")
#     for key in patient_keys:
#         patient_data = r.hgetall(key)
#         patients.append({k.decode(): v.decode() for k, v in patient_data.items()})

#     # Retrieve doctors
#     doctor_keys = r.keys("doctor:*")
#     for key in doctor_keys:
#         doctor_data = r.hgetall(key)
#         doctors.append({k.decode(): v.decode() for k, v in doctor_data.items()})

#     return patients, doctors

# # Get patients and doctors from Redis
# patients, doctors = get_patients_and_doctors()

# # Print the retrieved data
# #print(json.dumps(patient, indent=4))





# def find_doctor_by_specialty(specialty, doctors):
#     found_doctors = [doctor for doctor in doctors if doctor['specialty'] == specialty]
#     return found_doctors

# # Example: Retrieve patient by name
# patient_name = 'Bob'
# found_patient = find_patient_by_name(patient_name, patients)


# # Example: Retrieve doctors by specialty
# doctor_specialty = 'Neurology'
# found_doctors = find_doctor_by_specialty(doctor_specialty, doctors)
# for doctor in found_doctors:
#     print(doctor['name'])
