from sqlalchemy.orm import Session
import models, schemas


def get_mall(db: Session, mall_id: int):
    return db.query(models.Mall).filter(models.Mall.id == mall_id).first()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_complaint(db: Session, complaint_id: int):
    return db.query(models.Complaint).filter(models.Complaint.id == complaint_id).first()


def get_resolution(db: Session, resolution_id: int):
    return db.query(models.Resolution).filter(models.Resolution.id == resolution_id).first()


def get_malls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mall).offset(skip).limit(limit).all()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def get_complaints(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Complaint).offset(skip).limit(limit).all()


def get_resolutions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resolution).offset(skip).limit(limit).all()


def create_mall(db: Session, mall: schemas.MallCreate):
    db_mall = models.Mall(**mall.dict())
    db.add(db_mall)
    db.commit()
    db.refresh(db_mall)
    return db_mall


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def create_complaint(db: Session, complaint: schemas.ComplaintCreate):
    db_complaint = models.Complaint(**complaint.dict())
    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)
    return db_complaint


def create_resolution(db: Session, resolution: schemas.ResolutionCreate):
    db_resolution = models.Resolution(**resolution.dict())
    db.add(db_resolution)
    db.commit()
    db.refresh(db_resolution)
    return db_resolution

def update_mall(db: Session, mall_id: int, mall: schemas.MallCreate):
    db.query(models.Mall).filter(models.Mall.id == mall_id).update(mall.dict())
    db.commit()
    return db.query(models.Mall).filter(models.Mall.id == mall_id).first()


def delete_mall(db: Session, mall_id: int):
    db.query(models.Mall).filter(models.Mall.id == mall_id).delete()
    db.commit()


def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db.query(models.Employee).filter(models.Employee.id == employee_id).update(employee.dict())
    db.commit()
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def delete_employee(db: Session, employee_id: int):
    db.query(models.Employee).filter(models.Employee.id == employee_id).delete()
    db.commit()


def update_customer(db: Session, customer_id: int, customer: schemas.CustomerCreate):
    db.query(models.Customer).filter(models.Customer.id == customer_id).update(customer.dict())
    db.commit()
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def delete_customer(db: Session, customer_id: int):
    db.query(models.Customer).filter(models.Customer.id == customer_id).delete()
    db.commit()


def update_complaint(db: Session, complaint_id: int, complaint: schemas.ComplaintCreate):
    db.query(models.Complaint).filter(models.Complaint.id == complaint_id).update(complaint.dict())
    db.commit()
    return db.query(models.Complaint).filter(models.Complaint.id == complaint_id).first()


def delete_complaint(db: Session, complaint_id: int):
    db.query(models.Complaint).filter(models.Complaint.id == complaint_id).delete()
    db.commit()


def update_resolution(db: Session, resolution_id: int, resolution: schemas.ResolutionCreate):
    db.query(models.Resolution).filter(models.Resolution.id == resolution_id).update(resolution.dict())
    db.commit()
    return db.query(models.Resolution).filter(models.Resolution.id == resolution_id).first()


def delete_resolution(db: Session, resolution_id: int):
    db.query(models.Resolution).filter(models.Resolution.id == resolution_id).delete()
    db.commit()

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Department).offset(skip).limit(limit).all()

def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def update_department(db: Session, department_id: int, department: schemas.DepartmentCreate):
    db.query(models.Department).filter(models.Department.id == department_id).update(department.dict())
    db.commit()
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def delete_department(db: Session, department_id: int):
    db.query(models.Department).filter(models.Department.id == department_id).delete()
    db.commit()