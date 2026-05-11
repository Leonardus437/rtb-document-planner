"""
COMPLETE PYTHONANYWHERE BACKEND - COPY TO main.py
Fixes: Document creation endpoints + User profile data
"""

from flask import Flask, jsonify, request, make_response, send_file
from flask_cors import CORS
import tempfile
import os
from datetime import datetime

app = Flask(__name__)

# CORS configuration
CORS(app, 
     resources={r"/*": {"origins": "*"}},
     allow_headers=["Content-Type", "Authorization", "Accept"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     supports_credentials=False)

# In-memory database
users_db = {}
session_plans_db = {}
schemes_db = {}
next_plan_id = 1
next_scheme_id = 1

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Accept')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify({
        "message": "RTB Document Planner API", 
        "status": "online", 
        "version": "2.1",
        "endpoints": ["register", "login", "session-plans", "schemes"]
    })

@app.route('/users/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        name = data.get('name')
        
        if not phone or not name:
            return jsonify({"detail": "Phone and name required"}), 400
        
        if phone in users_db:
            return jsonify({"detail": "Phone number already registered"}), 400
        
        # Store complete user data
        users_db[phone] = {
            "user_id": data.get('user_id', f"USER_{len(users_db)+1}"),
            "name": name,
            "phone": phone,
            "email": data.get('email', ''),
            "institution": data.get('institution', ''),
            "password": data.get('password', 'default123'),
            "role": "user",
            "is_premium": False,
            "session_plans_limit": 2,
            "schemes_limit": 2,
            "session_plans_downloaded": 0,
            "schemes_downloaded": 0
        }
        
        return jsonify({"message": "User registered successfully"}), 201
        
    except Exception as e:
        return jsonify({"detail": f"Registration error: {str(e)}"}), 500

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        
        if phone in users_db:
            user = users_db[phone]
            return jsonify({
                "user_id": user["user_id"],
                "name": user["name"],
                "phone": phone,
                "email": user["email"],
                "institution": user["institution"],
                "role": user["role"],
                "is_premium": user["is_premium"],
                "session_plans_limit": user["session_plans_limit"],
                "schemes_limit": user["schemes_limit"]
            }), 200
        else:
            # Create demo user for testing
            demo_user = {
                "user_id": f"DEMO_{phone[-4:]}",
                "name": "Demo Teacher",
                "phone": phone,
                "email": "demo@school.rw",
                "institution": "Demo School",
                "role": "user",
                "is_premium": False,
                "session_plans_limit": 2,
                "schemes_limit": 2,
                "session_plans_downloaded": 0,
                "schemes_downloaded": 0
            }
            users_db[phone] = demo_user
            return jsonify(demo_user), 200
            
    except Exception as e:
        return jsonify({"detail": f"Login error: {str(e)}"}), 500

@app.route('/user-limits/<phone>', methods=['GET', 'OPTIONS'])
def user_limits(phone):
    if request.method == 'OPTIONS':
        return '', 204
    
    if phone in users_db:
        user = users_db[phone]
        return jsonify({
            "session_plans_limit": user["session_plans_limit"],
            "schemes_limit": user["schemes_limit"],
            "session_plans_downloaded": user["session_plans_downloaded"],
            "schemes_downloaded": user["schemes_downloaded"],
            "is_premium": user["is_premium"],
            "session_plans_remaining": max(0, user["session_plans_limit"] - user["session_plans_downloaded"]),
            "schemes_remaining": max(0, user["schemes_limit"] - user["schemes_downloaded"])
        })
    
    return jsonify({
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "session_plans_downloaded": 0,
        "schemes_downloaded": 0,
        "is_premium": False,
        "session_plans_remaining": 2,
        "schemes_remaining": 2
    })

# NEW: Session Plans endpoints
@app.route('/session-plans/', methods=['POST', 'OPTIONS'])
def create_session_plan():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        global next_plan_id
        data = request.get_json()
        
        plan_id = next_plan_id
        next_plan_id += 1
        
        # Store session plan
        session_plans_db[plan_id] = {
            "id": plan_id,
            "created_at": datetime.now().isoformat(),
            **data
        }
        
        return jsonify({"id": plan_id, "message": "Session plan created successfully"}), 201
        
    except Exception as e:
        return jsonify({"detail": f"Error creating session plan: {str(e)}"}), 500

@app.route('/session-plans/<int:plan_id>/download', methods=['GET', 'OPTIONS'])
def download_session_plan(plan_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        if plan_id not in session_plans_db:
            return jsonify({"detail": "Session plan not found"}), 404
        
        plan = session_plans_db[plan_id]
        
        # Update download counter
        phone = request.args.get('phone')
        if phone and phone in users_db:
            users_db[phone]["session_plans_downloaded"] += 1
        
        # Generate simple text file (replace with DOCX generation later)
        content = f"""RTB SESSION PLAN
        
Topic: {plan.get('topic_of_session', 'N/A')}
Trainer: {plan.get('trainer_name', 'N/A')}
Date: {plan.get('date', 'N/A')}
Duration: {plan.get('duration', '40')} minutes

Learning Outcomes:
{plan.get('learning_outcomes', 'N/A')}

Indicative Contents:
{plan.get('indicative_contents', 'N/A')}

Generated by RTB Document Planner
"""
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        temp_file.write(content)
        temp_file.close()
        
        return send_file(
            temp_file.name,
            as_attachment=True,
            download_name=f"session_plan_{plan_id}.txt",
            mimetype='text/plain'
        )
        
    except Exception as e:
        return jsonify({"detail": f"Download error: {str(e)}"}), 500

# NEW: Schemes endpoints
@app.route('/schemes/', methods=['POST', 'OPTIONS'])
def create_scheme():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        global next_scheme_id
        data = request.get_json()
        
        scheme_id = next_scheme_id
        next_scheme_id += 1
        
        # Store scheme
        schemes_db[scheme_id] = {
            "id": scheme_id,
            "created_at": datetime.now().isoformat(),
            **data
        }
        
        return jsonify({"id": scheme_id, "message": "Scheme of work created successfully"}), 201
        
    except Exception as e:
        return jsonify({"detail": f"Error creating scheme: {str(e)}"}), 500

@app.route('/schemes/<int:scheme_id>/download', methods=['GET', 'OPTIONS'])
def download_scheme(scheme_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        if scheme_id not in schemes_db:
            return jsonify({"detail": "Scheme not found"}), 404
        
        scheme = schemes_db[scheme_id]
        
        # Update download counter
        phone = request.args.get('phone')
        if phone and phone in users_db:
            users_db[phone]["schemes_downloaded"] += 1
        
        # Generate simple text file
        content = f"""RTB SCHEME OF WORK

School: {scheme.get('school', 'N/A')}
Trainer: {scheme.get('trainer_name', 'N/A')}
Module: {scheme.get('module_code_title', 'N/A')}
RQF Level: {scheme.get('rqf_level', 'N/A')}

Term 1 Learning Outcomes:
{scheme.get('term1_learning_outcomes', 'N/A')}

Term 2 Learning Outcomes:
{scheme.get('term2_learning_outcomes', 'N/A')}

Term 3 Learning Outcomes:
{scheme.get('term3_learning_outcomes', 'N/A')}

Generated by RTB Document Planner
"""
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        temp_file.write(content)
        temp_file.close()
        
        return send_file(
            temp_file.name,
            as_attachment=True,
            download_name=f"scheme_of_work_{scheme_id}.txt",
            mimetype='text/plain'
        )
        
    except Exception as e:
        return jsonify({"detail": f"Download error: {str(e)}"}), 500

# Admin endpoints
@app.route('/users/', methods=['GET', 'OPTIONS'])
def get_users():
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify(list(users_db.values()))

@app.route('/stats', methods=['GET', 'OPTIONS'])
def get_stats():
    if request.method == 'OPTIONS':
        return '', 204
    
    total_users = len(users_db)
    premium_users = sum(1 for u in users_db.values() if u.get("is_premium", False))
    
    return jsonify({
        "total_users": total_users,
        "premium_users": premium_users,
        "free_users": total_users - premium_users,
        "total_session_plans": len(session_plans_db),
        "total_schemes": len(schemes_db),
        "total_downloads": sum(u.get("session_plans_downloaded", 0) + u.get("schemes_downloaded", 0) for u in users_db.values())
    })

if __name__ == '__main__':
    app.run()