from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi import FastAPI, Request, Response

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Malls
@app.get("/malls/", response_model=list[schemas.Mall])
def read_malls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    malls = crud.get_malls(db, skip=skip, limit=limit)
    return malls

@app.post("/malls/", response_model=schemas.Mall)
def create_mall(mall: schemas.MallCreate, db: Session = Depends(get_db)):
    return crud.create_mall(db=db, mall=mall)

@app.put("/malls/{mall_id}", response_model=schemas.Mall)
def update_mall(mall_id: int, mall: schemas.MallUpdate, db: Session = Depends(get_db)):
    return crud.update_mall(db=db, mall_id=mall_id, mall=mall)

@app.delete("/malls/{mall_id}")
def delete_mall(mall_id: int, db: Session = Depends(get_db)):
    crud.delete_mall(db, mall_id)
    return {"message": "Mall deleted successfully"}
# Departments
@app.get("/departments/", response_model=list[schemas.Department])
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = crud.get_departments(db, skip=skip, limit=limit)
    return departments

@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)

@app.put("/departments/{department_id}", response_model=schemas.Department)
def update_department(department_id: int, department: schemas.DepartmentUpdate, db: Session = Depends(get_db)):
    return crud.update_department(db=db, department_id=department_id, department=department)

@app.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    crud.delete_department(db, department_id)
    return {"message": "Department deleted successfully"}

# Employees
@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, employee_id=employee_id, employee=employee)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db, employee_id)
    return {"message": "Employee deleted successfully"}

# Customers
@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers

@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    return crud.update_customer(db=db, customer_id=customer_id, customer=customer)

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    crud.delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}

# Complaints
@app.get("/complaints/", response_model=list[schemas.Complaint])
def read_complaints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    complaints = crud.get_complaints(db, skip=skip, limit=limit)
    return complaints

@app.post("/complaints/", response_model=schemas.Complaint)
def create_complaint(complaint: schemas.ComplaintCreate, db: Session = Depends(get_db)):
    return crud.create_complaint(db=db, complaint=complaint)

@app.put("/complaints/{complaint_id}", response_model=schemas.Complaint)
def update_complaint(complaint_id: int, complaint: schemas.ComplaintUpdate, db: Session = Depends(get_db)):
    return crud.update_complaint(db=db, complaint_id=complaint_id, complaint=complaint)

@app.delete("/complaints/{complaint_id}")
def delete_complaint(complaint_id: int, db: Session = Depends(get_db)):
    crud.delete_complaint(db, complaint_id)
    return {"message": "Complaint deleted successfully"}

# Resolutions
@app.get("/resolutions/", response_model=list[schemas.Resolution])
def read_resolutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resolutions = crud.get_resolutions(db, skip=skip, limit=limit)
    return resolutions

@app.post("/resolutions/", response_model=schemas.Resolution)
def create_resolution(resolution: schemas.ResolutionCreate, db: Session = Depends(get_db)):
    return crud.create_resolution(db=db, resolution=resolution)

@app.put("/resolutions/{resolution_id}", response_model=schemas.Resolution)
def update_resolution(resolution_id: int, resolution: schemas.ResolutionUpdate, db: Session = Depends(get_db)):
    return crud.update_resolution(db=db, resolution_id=resolution_id, resolution=resolution)

@app.delete("/resolutions/{resolution_id}")
def delete_resolution(resolution_id: int, db: Session = Depends(get_db)):
    crud.delete_resolution(db, resolution_id)
    return {"message": "Resolution deleted successfully"}


