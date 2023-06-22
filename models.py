from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql.expression import text


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Mall(Base):
    __tablename__ = "malls"

    id = Column(Integer, primary_key=True, unique=True, server_default=text("(random() * 8999 + 1000)::int"))
    name = Column(String, index=True)
    location = Column(String)
    contact = Column(String)

    departments = relationship("Department", back_populates="mall")

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, unique=True, server_default=text("(random() * 8999 + 1000)::int"))
    mall_id = Column(Integer, ForeignKey("malls.id"))
    name = Column(String)
    contact = Column(String)

    mall = relationship("Mall", back_populates="departments")
    employees = relationship("Employee", back_populates="department")
    complaints = relationship("Complaint", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, unique=True, server_default=text("(random() * 8999 + 1000)::int"))
    name = Column(String)
    contact = Column(String)
    email = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")
    complaints = relationship("Complaint", back_populates="employee")
    resolutions = relationship("Resolution", back_populates="employee")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, unique=True, server_default=text("(random() * 8999 + 1000)::int"))
    name = Column(String)
    contact = Column(String)
    email = Column(String)

    complaints = relationship("Complaint", back_populates="customer")


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, unique=True, server_default=text("(random() * 8999 + 1000)::int"))
    department_id = Column(Integer, ForeignKey("departments.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    category = Column(String)
    details = Column(String)
    date = Column(String)
    status = Column(String)
    priority = Column(String)

    department = relationship("Department", back_populates="complaints")
    customer = relationship("Customer", back_populates="complaints")
    employee = relationship("Employee", back_populates="complaints")
    resolution = relationship("Resolution", back_populates="complaint", uselist=False)

class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True, unique=True, server_default=text("(random() * 8999 + 1000)::int"))
    complaint_id = Column(Integer, ForeignKey("complaints.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    details = Column(String)
    date = Column(String)
    status = Column(String)

    complaint = relationship("Complaint", back_populates="resolution")
    employee = relationship("Employee", back_populates="resolutions")

