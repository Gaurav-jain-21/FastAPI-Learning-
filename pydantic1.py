from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name:str = Annotated[str, Field(max_length=50, title="name of the patient",examples=['Gaurav','Ram','Vikash'])]   #Field(max_leagth=30)
    email: EmailStr
    linkedin_url: AnyUrl
    age:int= Field(gt=0, lt=120)
    weight: float=Field(gt=0)
    married: Annotated[bool, Field(default=None, description="is the patient married or not")]
    allergies: Annotated[Optional[List[str]],Field(max_length=5,default=None)]
    contact: Dict[str, str]
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("inserted")    

patient_info={'name': "garuav",'email':"abc@gmail.com",'linkedin_url':"https://monkeytype.com/" ,'age':30, 'weight':70.0,'married':True,'contact':{"rame":"94632","weviohg":"945123"}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)