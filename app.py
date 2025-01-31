from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# In-memory storage (in a real app, this would be a database)
students = {}
assignments = {}
feedback = {}

@app.route('/api/students', methods=['GET', 'POST'])
def handle_students():
    if request.method == 'GET':
        return jsonify(list(students.values()))
    
    if request.method == 'POST':
        data = request.json
        student_id = str(len(students) + 1)
        student = {
            'id': student_id,
            'name': data['name'],
            'email': data['email'],
            'progress': 0,
            'created_at': datetime.now().isoformat()
        }
        students[student_id] = student
        return jsonify(student), 201

@app.route('/api/assignments', methods=['GET', 'POST'])
def handle_assignments():
    if request.method == 'GET':
        return jsonify(list(assignments.values()))
    
    if request.method == 'POST':
        data = request.json
        assignment_id = str(len(assignments) + 1)
        assignment = {
            'id': assignment_id,
            'title': data['title'],
            'description': data['description'],
            'due_date': data['due_date'],
            'topic': data['topic'],
            'difficulty': data['difficulty'],
            'created_at': datetime.now().isoformat()
        }
        assignments[assignment_id] = assignment
        return jsonify(assignment), 201

@app.route('/api/students/<student_id>/progress', methods=['GET', 'PUT'])
def handle_student_progress(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student not found'}), 404
        
    if request.method == 'GET':
        return jsonify({
            'student': students[student_id],
            'progress': students[student_id]['progress']
        })
    
    if request.method == 'PUT':
        data = request.json
        students[student_id]['progress'] = data['progress']
        return jsonify(students[student_id])

@app.route('/api/assignments/<assignment_id>/feedback', methods=['POST', 'GET'])
def handle_feedback(assignment_id):
    if assignment_id not in assignments:
        return jsonify({'error': 'Assignment not found'}), 404
        
    if request.method == 'POST':
        data = request.json
        feedback_id = str(len(feedback) + 1)
        new_feedback = {
            'id': feedback_id,
            'assignment_id': assignment_id,
            'student_id': data['student_id'],
            'comment': data['comment'],
            'grade': data['grade'],
            'created_at': datetime.now().isoformat()
        }
        feedback[feedback_id] = new_feedback
        return jsonify(new_feedback), 201
    
    if request.method == 'GET':
        assignment_feedback = [f for f in feedback.values() 
                             if f['assignment_id'] == assignment_id]
        return jsonify(assignment_feedback)

@app.route('/api/analytics/dsa-progress', methods=['GET'])
def get_dsa_analytics():
    # Calculate average progress
    if not students:
        return jsonify({'average_progress': 0, 'total_students': 0})
    
    total_progress = sum(s['progress'] for s in students.values())
    average_progress = total_progress / len(students)
    
    return jsonify({
        'average_progress': average_progress,
        'total_students': len(students),
        'progress_distribution': {
            'beginner': len([s for s in students.values() if s['progress'] < 33]),
            'intermediate': len([s for s in students.values() if 33 <= s['progress'] < 66]),
            'advanced': len([s for s in students.values() if s['progress'] >= 66])
        }
    })

if __name__ == '__main__':
    app.run(debug=True)