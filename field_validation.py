from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
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
    @field_validator('name')
    @classmethod
    def name_email(cls,value):
        return value.upper()
    @field_validator('age', mode="after")
    @classmethod
    def validator_age(cls, value):
        if 0 < value<100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")
    @model_validator(mode='after')
    def validate_emergency_contact(cls,self):
        if self.age>60 and 'emergency' not in self.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return self   

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


patient_info={'name':'gaurav','email':'abc@hdfc.com', 'age':61,'weight':54.3,'married':True,'allergies':['wind','light','dust'],'contact_details':{'phone':"9876543210"}}
patient1=Patient(**patient_info)
update_patient_data(patient1)
