"""
Test script to demonstrate API usage
Run this after starting the server with: uvicorn main:app --reload
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def print_response(title, response):
    """Pretty print API responses"""
    print(f"\n{'='*60}")
    print(f"📌 {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")


def test_api():
    """Test all CRUD operations"""
    
    print("🚀 Starting Student Info API Tests...\n")
    
    # 1. CREATE - Add students
    print("\n1️⃣  CREATING STUDENTS...")
    
    students_data = [
        {
            "name": "Alice Johnson",
            "age": 20,
            "grade": "A",
            "email": "alice@university.edu",
            "gpa": 3.9
        },
        {
            "name": "Bob Smith",
            "age": 22,
            "grade": "B+",
            "email": "bob@university.edu",
            "gpa": 3.5
        },
        {
            "name": "Charlie Brown",
            "age": 19,
            "grade": "A-",
            "email": "charlie@university.edu",
            "gpa": 3.7
        }
    ]
    
    created_ids = []
    for student in students_data:
        response = requests.post(f"{BASE_URL}/students/", json=student)
        print_response(f"Created: {student['name']}", response)
        if response.status_code == 201:
            created_ids.append(response.json()['id'])
    
    # 2. READ - Get all students
    print("\n\n2️⃣  READING ALL STUDENTS...")
    response = requests.get(f"{BASE_URL}/students/")
    print_response("All Students", response)
    
    # 3. READ - Get single student
    if created_ids:
        print("\n\n3️⃣  READING SINGLE STUDENT...")
        response = requests.get(f"{BASE_URL}/students/{created_ids[0]}")
        print_response(f"Student with ID {created_ids[0]}", response)
    
    # 4. UPDATE - Update student
    if created_ids:
        print("\n\n4️⃣  UPDATING STUDENT...")
        update_data = {
            "gpa": 4.0,
            "grade": "A+"
        }
        response = requests.put(f"{BASE_URL}/students/{created_ids[0]}", json=update_data)
        print_response(f"Updated Student {created_ids[0]}", response)
    
    # 5. SEARCH - Search by name
    print("\n\n5️⃣  SEARCHING STUDENTS...")
    response = requests.get(f"{BASE_URL}/students/search/Alice")
    print_response("Search Results for 'Alice'", response)
    
    # 6. DELETE - Delete a student
    if len(created_ids) > 1:
        print("\n\n6️⃣  DELETING STUDENT...")
        response = requests.delete(f"{BASE_URL}/students/{created_ids[-1]}")
        print_response(f"Deleted Student {created_ids[-1]}", response)
        
        # Verify deletion
        response = requests.get(f"{BASE_URL}/students/")
        print_response("Students After Deletion", response)
    
    print("\n\n" + "="*60)
    print("✅ All tests completed!")
    print("="*60)
    print("\n💡 Tip: Visit http://127.0.0.1:8000/docs for interactive API documentation")


if __name__ == "__main__":
    try:
        # Test if server is running
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            test_api()
        else:
            print("❌ Server responded with an error")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to the API server!")
        print("📝 Make sure the server is running with: uvicorn main:app --reload")
    except Exception as e:
        print(f"❌ Error: {e}")
