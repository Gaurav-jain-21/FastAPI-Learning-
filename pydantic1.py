from pydantic import BaseModel
from typing import List, Dict, Optional
class Patient(BaseModel):
    name:str
    age:int
    weight: float
    married: bool
    allergies: Optional[List[str]]=None
    contact: Dict[str, str]
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("inserted")    

patient_info={'name': "garuav", 'age':30, 'weight':70.0,'married':True,'contact':{"rame":"94632","weviohg":"945123"}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)