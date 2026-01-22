from pydantic import BaseModel
class Address(BaseModel):
    city: str
    state: str
    pin: str
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict={'city': 'purena','state':'Bihar','pin':'854326'} 
addres1=Address(**address_dict)
patient_info={'name':'Gaurav Jain','gender':'male','age':21,'address':addres1}
patient1= Patient(**patient_info)
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)