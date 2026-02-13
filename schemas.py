from pydantic import BaseModel, EmailStr, Field, constr
from typing import Optional


class StudentBase(BaseModel):
    """Base schema with common fields"""
    name: str = Field(..., min_length=1, max_length=100, description="Student's full name")
    age: int = Field(..., ge=5, le=100, description="Student's age (5-100)")
    grade: str = Field(..., description="Student's grade (e.g., A, B, C)")
    email: EmailStr = Field(..., description="Student's email address")
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0, description="GPA (0.0-4.0)")
    phone: Optional[constr(pattern=r'^\d{10}$')] = Field(None, description="Student's phone number (10 digits)")


class StudentCreate(StudentBase):
    """Schema for creating a new student"""
    pass


class StudentUpdate(BaseModel):
    """Schema for updating a student - all fields optional"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, ge=5, le=100)
    grade: Optional[str] = None
    email: Optional[EmailStr] = None
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    phone: Optional[constr(pattern=r'^\d{10}$')] = Field(None, description="Student's phone number (10 digits)")
    

class StudentResponse(StudentBase):
    """Schema for student response - includes ID"""
    id: int
    
    class Config:
        from_attributes = True  # Allows ORM model to Pydantic model conversion
