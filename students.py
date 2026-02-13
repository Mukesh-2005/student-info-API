import requests

students = [
    {"name": "John", "age": 20, "grade": "A", "email": "john@test.com", "gpa": 3.8},
    {"name": "Jane", "age": 22, "grade": "B+", "email": "jane@test.com", "gpa": 3.5},
]

for student in students:
    response = requests.post("http://127.0.0.1:8000/students/", json=student)
    print(response.json())