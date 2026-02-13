# 🎓 Student Info API

A simple RESTful API built with FastAPI for managing student information with full CRUD operations.

## 📋 Features

- ✅ **Create** new students
- 📖 **Read** all students or a specific student
- ✏️ **Update** student information
- 🗑️ **Delete** students
- 🔍 **Search** students by name
- ✉️ Email validation and uniqueness
- 📊 GPA tracking (0.0-4.0 scale)

## 🛠️ Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL ORM for database operations
- **Pydantic** - Data validation
- **SQLite** - Lightweight database (no setup required!)

## 📁 Project Structure

```
student_info_api/
├── main.py           # FastAPI app with all endpoints
├── models.py         # Database models (Student table)
├── schemas.py        # Pydantic schemas for validation
├── database.py       # Database configuration
├── requirements.txt  # Dependencies
└── README.md         # This file
```

## 🚀 Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### 3. Access Interactive Docs

Open your browser and go to:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📚 API Endpoints

### Root
- `GET /` - Welcome message and API info

### Students

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students/` | Create a new student |
| GET | `/students/` | Get all students (with pagination) |
| GET | `/students/{student_id}` | Get a specific student by ID |
| PUT | `/students/{student_id}` | Update a student's information |
| DELETE | `/students/{student_id}` | Delete a student |
| GET | `/students/search/{name}` | Search students by name |

## 🧪 Testing the API

### 1. Create a Student (POST)

```bash
curl -X POST "http://127.0.0.1:8000/students/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "email": "john@example.com",
    "gpa": 3.8
  }'
```

### 2. Get All Students (GET)

```bash
curl "http://127.0.0.1:8000/students/"
```

### 3. Get Single Student (GET)

```bash
curl "http://127.0.0.1:8000/students/1"
```

### 4. Update Student (PUT)

```bash
curl -X PUT "http://127.0.0.1:8000/students/1" \
  -H "Content-Type: application/json" \
  -d '{
    "gpa": 3.9,
    "grade": "A+"
  }'
```

### 5. Delete Student (DELETE)

```bash
curl -X DELETE "http://127.0.0.1:8000/students/1"
```

### 6. Search Students (GET)

```bash
curl "http://127.0.0.1:8000/students/search/John"
```

## 📝 Request/Response Examples

### Create Student Request
```json
{
  "name": "Jane Smith",
  "age": 22,
  "grade": "B+",
  "email": "jane@example.com",
  "gpa": 3.5
}
```

### Response
```json
{
  "id": 1,
  "name": "Jane Smith",
  "age": 22,
  "grade": "B+",
  "email": "jane@example.com",
  "gpa": 3.5
}
```

## 🔍 Key Concepts Explained

### 1. **CRUD Operations**
- **C**reate: Add new student (POST)
- **R**ead: Get student(s) (GET)
- **U**pdate: Modify student info (PUT)
- **D**elete: Remove student (DELETE)

### 2. **ORM (SQLAlchemy)**
Instead of writing SQL:
```sql
INSERT INTO students VALUES (1, 'John', 20, 'A', 'john@email.com', 3.8);
```

You write Python:
```python
student = Student(name="John", age=20, grade="A", email="john@email.com", gpa=3.8)
db.add(student)
db.commit()
```

### 3. **Pydantic Validation**
Automatically validates:
- Age must be 5-100
- Email must be valid format
- GPA must be 0.0-4.0
- Name cannot be empty

### 4. **Dependency Injection**
`db: Session = Depends(get_db)` automatically:
- Creates database connection
- Gives it to your function
- Closes it when done

## ⚡ Quick Tips

1. **View Database**: The `students.db` SQLite file is created automatically
2. **Test Easily**: Use the `/docs` endpoint - it's interactive!
3. **Error Handling**: API returns proper HTTP status codes and error messages
4. **Pagination**: Use `?skip=0&limit=10` on GET /students/

## 🎯 What You Learned

- ✅ Setting up FastAPI with database
- ✅ Creating database models with SQLAlchemy
- ✅ Data validation with Pydantic
- ✅ All CRUD operations
- ✅ Error handling and HTTP status codes
- ✅ API documentation (auto-generated!)

## 🚀 Next Steps

1. Add authentication (JWT tokens)
2. Add more fields (phone, address, courses)
3. Add filtering (by grade, age range)
4. Deploy to cloud (Heroku, AWS, etc.)
5. Add tests with pytest

## 📄 License

Free to use for learning purposes!

---

**Happy Coding! 🎉**
