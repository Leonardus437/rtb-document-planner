import requests
import json

# Test data
data = {
    "sector": "ICT",
    "trade": "Software Development",
    "rqf_level": "Level 4",
    "date": "2025-01-20",
    "trainer_name": "Test Teacher",
    "term": "Term 1",
    "module_code_title": "Programming Basics",
    "week": "Week 1",
    "number_of_trainees": "25",
    "class_name": "L4CSA",
    "topic_of_session": "Variables",
    "learning_outcomes": "Apply programming concepts",
    "indicative_contents": "Variables, data types",
    "session_range": "Basic to intermediate",
    "facilitation_techniques": "Trainer Guided",
    "duration": "40"
}

print("Testing session plan creation...")
try:
    response = requests.post(
        "http://localhost:5000/session-plans/",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
