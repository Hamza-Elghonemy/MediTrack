import redis
import json
import socket
import numpy as np
 

redis_host='redis-17832.c281.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 17832
password = "Hamza123"
r = redis.Redis(redis_host,redis_port, db=0, password=password)
  
def load_data_from_json(json_file):
    with open(json_file) as f:
        return json.load(f)

def store_patients(patients):
    # Generate a unique key for the patient data
    patient_id = r.incr('patient_id_counter')
    # Store the JSON data in a hash
    r.hmset(f'patient:{patient_id}', patients)
    print(f"Patient data stored with ID: {patient_id}")
    return patient_id
    
def update_diagnosis(patient_id, vitalsign):
    # Check if the patient exists
    if r.exists(f'patient:{patient_id}'):
        # Update the diagnosis in the hash
        r.hset(f'patient:{patient_id}', 'vitalSign', vitalsign)
        print(f"Diagnosis updated for patient with ID: {patient_id}")
    else:
        print(f"Patient with ID {patient_id} doesn't exist")
    
def server_program():
    host = 'localhost'
    port = 5000  # initiate port number above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(4)
    while True:
        
        conn, address = server_socket.accept()  # accept new connection 
        data = conn.recv(1024).decode()
        user_data = json.loads(data)
        #if len(user_data) >2:
        patient_id = store_patients(user_data)
        #else:
            # # Check if the received data has a patient ID
            # if 'username' in user_data and 'vitalSign' in user_data:
            #     vitalsign = user_data['vitalSign']
            #     update_diagnosis(patient_id, vitalsign)
        server_data = "recieved"
        conn.send(server_data.encode())  # send data to the client
        
if __name__ == '__main__':
    server_program()

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



# def find_patient_by_name(name, patients):
#     for patient in patients:
#         if patient['name'] == name:
#             return patient
#     return None

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
