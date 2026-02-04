import requests
import json

BASE_URL = "http://localhost:5000"

print("="*60)
print("TESTING TEACHER WORKFLOW")
print("="*60)

# Test 1: Backend is running
print("\n[1/4] Testing backend connection...")
try:
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        print("[OK] Backend is running")
    else:
        print("[FAIL] Backend not responding")
        exit()
except:
    print("[FAIL] Cannot connect to backend")
    exit()

# Test 2: Create session plan
print("\n[2/4] Testing session plan creation...")
session_data = {
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

try:
    response = requests.post(
        f"{BASE_URL}/session-plans/",
        json=session_data,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        result = response.json()
        plan_id = result.get('id')
        print(f"[OK] Session plan created (ID: {plan_id})")
    else:
        print(f"[FAIL] Failed to create session plan: {response.status_code}")
        print(f"   Error: {response.text}")
        exit()
except Exception as e:
    print(f"[FAIL] Error: {e}")
    exit()

# Test 3: Download session plan
print("\n[3/4] Testing document download...")
try:
    response = requests.get(f"{BASE_URL}/session-plans/{plan_id}/download")
    if response.status_code == 200:
        with open(f"test_session_plan_{plan_id}.docx", "wb") as f:
            f.write(response.content)
        print(f"[OK] Document downloaded: test_session_plan_{plan_id}.docx")
    else:
        print(f"[FAIL] Failed to download: {response.status_code}")
except Exception as e:
    print(f"[FAIL] Error: {e}")

# Test 4: Check CORS
print("\n[4/4] Testing CORS configuration...")
try:
    response = requests.options(
        f"{BASE_URL}/session-plans/",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "POST"
        }
    )
    if response.status_code == 200:
        print("[OK] CORS is configured correctly")
    else:
        print("[FAIL] CORS issue detected")
except Exception as e:
    print(f"[FAIL] Error: {e}")

print("\n" + "="*60)
print("TEST COMPLETE!")
print("="*60)
print("\nIf all tests passed, teachers can create session plans!")
print("Go to: http://localhost:5173/wizard.html")
