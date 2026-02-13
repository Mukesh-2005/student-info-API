from sqlalchemy import Column, Integer, String, Float
from database import Base


class Student(Base):
    """
    Student model - represents the students table in database
    """
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    gpa = Column(Float, nullable=True)  # Grade Point Average (optional)
    phone = Column(String(10), nullable=True, index=True)