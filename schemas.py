from typing import List, Optional
from pydantic import BaseModel

class MallBase(BaseModel):
    name: str
    location: str
    contact: str

class MallCreate(MallBase):
    pass

class MallUpdate(MallBase):
    pass

class Mall(MallBase):
    id: int

    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    mall_id: int
    name: str
    contact: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    contact: str
    email: str
    department_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str
    contact: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class ComplaintBase(BaseModel):
    department_id: int
    customer_id: int
    employee_id: int
    category: str
    details: str
    date: str
    status: str
    priority: str

class ComplaintCreate(ComplaintBase):
    pass

class ComplaintUpdate(ComplaintBase):
    pass

class Complaint(ComplaintBase):
    id: int

    class Config:
        orm_mode = True

class ResolutionBase(BaseModel):
    complaint_id: int
    employee_id: int
    details: str
    date: str
    status: str

class ResolutionCreate(ResolutionBase):
    pass

class ResolutionUpdate(ResolutionBase):
    pass

class Resolution(ResolutionBase):
    id: int

    class Config:
        orm_mode = True
