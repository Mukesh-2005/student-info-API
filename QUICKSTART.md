# 🚀 Quick Start Guide

## Step 1: Install Dependencies (30 seconds)

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## Step 2: Start the Server (10 seconds)

```bash
uvicorn main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Step 3: Test It! (Choose one)

### Option A: Use the Interactive Docs (EASIEST!) 🎯

1. Open your browser
2. Go to: http://127.0.0.1:8000/docs
3. Click on any endpoint (e.g., "POST /students/")
4. Click "Try it out"
5. Edit the example data
6. Click "Execute"
7. See the response!

### Option B: Use the Test Script 🧪

Open a NEW terminal (keep server running) and run:
```bash
python test_api.py
```

### Option C: Use cURL 💻

Create a student:
```bash
curl -X POST "http://127.0.0.1:8000/students/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Student",
    "age": 20,
    "grade": "A",
    "email": "test@example.com",
    "gpa": 3.8
  }'
```

Get all students:
```bash
curl "http://127.0.0.1:8000/students/"
```

## 🎓 Understanding the Code

### 1. **database.py** - Database Setup
```python
# Creates SQLite database connection
engine = create_engine("sqlite:///./students.db")
```

### 2. **models.py** - Table Structure
```python
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # ... more fields
```

### 3. **schemas.py** - Data Validation
```python
class StudentCreate(BaseModel):
    name: str
    age: int  # Will validate age is a number
    email: EmailStr  # Will validate email format
```

### 4. **main.py** - API Endpoints
```python
@app.post("/students/")  # CREATE
@app.get("/students/")   # READ all
@app.get("/students/{id}")  # READ one
@app.put("/students/{id}")  # UPDATE
@app.delete("/students/{id}")  # DELETE
```

## 🔥 Try These Examples

### Example 1: Create Multiple Students

```python
import requests

students = [
    {"name": "John", "age": 20, "grade": "A", "email": "john@test.com", "gpa": 3.8},
    {"name": "Jane", "age": 22, "grade": "B+", "email": "jane@test.com", "gpa": 3.5},
]

for student in students:
    response = requests.post("http://127.0.0.1:8000/students/", json=student)
    print(response.json())
```

### Example 2: Update a Student

```python
import requests

# Update student with ID 1
update_data = {"gpa": 4.0, "grade": "A+"}
response = requests.put("http://127.0.0.1:8000/students/1", json=update_data)
print(response.json())
```

### Example 3: Search Students

```python
import requests

# Search for students with "John" in name
response = requests.get("http://127.0.0.1:8000/students/search/John")
print(response.json())
```

## 🐛 Common Issues

### Issue 1: Port Already in Use
```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

### Issue 2: Module Not Found
```bash
# Make sure you're in the project directory
cd student_info_api
pip install -r requirements.txt
```

### Issue 3: Database Locked
```bash
# Stop the server (CTRL+C) and restart
uvicorn main:app --reload
```

## 📊 What's Happening Behind the Scenes?

1. **You create a student** → FastAPI validates data → SQLAlchemy saves to database
2. **Database file created** → `students.db` appears in your folder
3. **Tables created automatically** → SQLAlchemy creates the `students` table
4. **Data persists** → Even after restarting, your data is saved!

## 🎯 Next Challenge

Try adding a new field! For example, add a "major" field:

1. Add to `models.py`: `major = Column(String, nullable=True)`
2. Add to `schemas.py`: `major: Optional[str] = None`
3. Restart server
4. Test it!

## 💡 Pro Tips

- Use `/docs` - it's your best friend for testing
- Check `students.db` - you can open it with SQLite browser
- Read the terminal logs - they show what's happening
- Hit CTRL+C to stop the server

---

**You're ready! Start the server and try it out! 🚀**
