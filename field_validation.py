from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain=["hdfc.com",'icici.com']
        domain_name=value.split("@")[-1]
        if(domain_name not in valid_domain):
            raise ValueError('Not a valid domain')
        return value


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


patient_info={'name':'gaurav','email':'abc@hdfc.com', 'age':30,'weight':54.3,'married':True,'allergies':['wind','light','dust'],'contact_details':{'phone':"9876543210"}}
patient1=Patient(**patient_info)
update_patient_data(patient1)
