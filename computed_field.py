from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.bmi)

patient_info={'name':'gaurav','email':'abc@gmail.com', 'age':61,'weight':70.3,'height':1.725,'married':True,'allergies':['wind','light','dust'],'contact_details':{'phone':"9876543210",'emergency':"987413"}}
patient1=Patient(**patient_info)
insert_patient(patient1)