from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Student Info API",
    description="A simple CRUD API for managing student information",
    version="1.0.0"
)


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Student Info API!",
        "docs": "/docs",
        "endpoints": {
            "create": "POST /students/",
            "read_all": "GET /students/",
            "read_one": "GET /students/{student_id}",
            "update": "PUT /students/{student_id}",
            "delete": "DELETE /students/{student_id}"
        }
    }


# CREATE - Add a new student
@app.post("/students/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Students"])
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student with the following information:
    - **name**: Student's full name
    - **age**: Student's age (5-100)
    - **grade**: Student's grade
    - **email**: Student's email (must be unique)
    - **gpa**: Grade Point Average (optional, 0.0-4.0)
    """
    # Check if email already exists
    existing_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Student with email {student.email} already exists"
        )
    
    # Create new student instance
    new_student = models.Student(**student.model_dump())
    
    # Add to database
    db.add(new_student)
    db.commit()
    db.refresh(new_student)  # Refresh to get the ID
    
    return new_student


# READ - Get all students
@app.get("/students/", response_model=List[schemas.StudentResponse], tags=["Students"])
def get_all_students(skip: int = 0, limit: int = 100,min_age: Optional[int] = None, max_age: Optional[int] = None, db: Session = Depends(get_db)):
    """
    Retrieve all students with pagination:
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 100)
    - **min_age**: Minimum age of students to retrieve (default: 0)
    - **max_age**: Maximum age of students to retrieve (default: 100)
    """
    query = db.query(models.Student)
    if min_age is not None:
        query = query.filter(models.Student.age >= min_age)
    if max_age is not None:
        query = query.filter(models.Student.age <= max_age)
    students = query.offset(skip).limit(limit).all()
    return students

@app.get("/students/grade/{grade}", response_model=List[schemas.StudentResponse], tags=["Students"])
def get_students_by_grade(grade: str, db: Session = Depends(get_db)):
    """
    Retrieve all students in a specific grade
    """
    students = db.query(models.Student).filter(models.Student.grade == grade).all()
    return students

@app.get("/students/search/{name}", response_model=List[schemas.StudentResponse], tags=["Students"])
def search_students(name: str, db: Session = Depends(get_db)):
    """
    Search for students by name (partial match)
    """
    students = db.query(models.Student).filter(models.Student.name.contains(name)).all()
    return students


# READ - Get a single student by ID
@app.get("/students/{student_id}", response_model=schemas.StudentResponse, tags=["Students"])
def get_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific student by their ID
    """
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    return student


# UPDATE - Update student information
@app.put("/students/{student_id}", response_model=schemas.StudentResponse, tags=["Students"])
def update_student(student_id: int, student_update: schemas.StudentUpdate, db: Session = Depends(get_db)):
    """
    Update a student's information. Only provided fields will be updated.
    """
    # Find the student
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    # Update only the fields that were provided
    update_data = student_update.model_dump(exclude_unset=True)
    
    # Check if email is being updated and if it's already taken
    if "email" in update_data:
        existing_student = db.query(models.Student).filter(
            models.Student.email == update_data["email"],
            models.Student.id != student_id
        ).first()
        if existing_student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email {update_data['email']} is already taken"
            )
    
    # Update fields
    for key, value in update_data.items():
        setattr(student, key, value)
    
    db.commit()
    db.refresh(student)
    
    return student


# DELETE - Remove a student
@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Students"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """
    Delete a student from the database
    """
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    db.delete(student)
    db.commit()
    
    return None



# BONUS: Search students by name
