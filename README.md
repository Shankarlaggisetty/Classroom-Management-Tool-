# Classroom Management API

A Flask-based REST API for managing student assignments and tracking DSA progress.

## API Endpoints

### Students
- `GET /api/students` - Get all students
- `POST /api/students` - Create a new student
- `GET /api/students/<id>/progress` - Get student's progress
- `PUT /api/students/<id>/progress` - Update student's progress

### Assignments
- `GET /api/assignments` - Get all assignments
- `POST /api/assignments` - Create a new assignment
- `POST /api/assignments/<id>/feedback` - Add feedback to assignment
- `GET /api/assignments/<id>/feedback` - Get feedback for assignment

### Analytics
- `GET /api/analytics/dsa-progress` - Get DSA progress analytics

## Setup and Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python app.py
   ```

The server will start on `http://localhost:5000`

## API Examples

### Create a Student
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Create an Assignment
```bash
curl -X POST http://localhost:5000/api/assignments \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Binary Search Implementation",
    "description": "Implement binary search algorithm",
    "due_date": "2024-03-20",
    "topic": "Searching Algorithms",
    "difficulty": "Medium"
  }'
```