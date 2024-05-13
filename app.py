from server import *


s =servers()

def search_Patient(name, password = None):
    patients = s.get_patients_and_doctors()
    current_patient = s.find_patient(name, password= password, patients = patients)
    return current_patient
    
def filterPatients( filter, current_sign):
    try:
        patients = s.get_patients_and_doctors()
        Patient_lists = s.filterPatients(patients=patients, sign= current_sign, filtration= filter)
    except Exception as e:
        print(f"error filtration inside app file : {e}")
    return Patient_lists