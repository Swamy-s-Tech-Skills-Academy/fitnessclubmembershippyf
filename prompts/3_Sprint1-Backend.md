# 🏗️ Sprint 1: Backend Foundation (15 minutes)

## 🎯 **COPY-PASTE PROMPT FOR SPRINT 1**

````text
Build a complete Flask backend for a fitness club membership system with the following requirements:

PYTHON VERSION REQUIREMENT:
- Python 3.13.5 (ensure compatibility with all Flask 3.0.0 and SQLAlchemy 2.0.35 features)

CRITICAL: REPLACE THE EXISTING SIMPLE WELCOME APP
The current src\app.py only contains a basic welcome page. You must REPLACE it entirely with a full application containing all the routes and functionality listed below.

MODELS NEEDED:
1. Member (id, first_name, last_name, email, phone, date_of_birth, gender, emergency_contact, emergency_phone, join_date, status)
2. MembershipPlan (id, name, description, monthly_price, benefits)
3. Trainer (id, name, specialization, email, phone)
4. WorkoutSession (id, title, description, trainer_id, session_date, start_time, end_time, max_capacity, current_bookings)
5. MemberPlan (id, member_id, plan_id, start_date, end_date, status)
6. SessionBooking (id, member_id, session_id, booking_date, status)

FILES TO CREATE/REPLACE:
- src\models.py (NEW: SQLAlchemy models with relationships)
- src\config.py (NEW: Flask configuration with ABSOLUTE database path)
- src\app.py (REPLACE: Complete Flask app with all routes - replaces existing welcome app)
- src\init_db.py (NEW: Database initialization with sample data)

IMPORTANT: REPLACE THE EXISTING SIMPLE WELCOME APP
The current src\app.py only has a welcome page. Replace it entirely with the full application.

REQUIRED APP.PY STRUCTURE:
```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Member, MembershipPlan, Trainer, WorkoutSession, MemberPlan, SessionBooking
import config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# Dashboard route (replaces welcome page)
@app.route('/')
def dashboard():
    # Statistics calculations here
    return render_template('dashboard.html', stats=stats)

# Member management routes
@app.route('/members')
def members_list():
    # Members list logic
    return render_template('members/list.html', members=members)

@app.route('/members/create')
def members_create():
    # Member creation form
    return render_template('members/create.html')

# Continue with other routes...
````

EXACT ROUTES TO IMPLEMENT:

- / (dashboard with statistics: total members, active sessions, revenue, growth)
- /members (list with search functionality)
- /members/create (member registration form)
- /members/\<id\> (member details view)
- /members/\<id\>/edit (member edit form)
- /plans (membership plans display)
- /sessions (workout sessions list)
- /sessions/schedule (session scheduling form)

IMPORTANT DATABASE PATH CONFIG:
In config.py, use absolute path to prevent "unable to open database file" error:

```python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "instance", "fitness_club.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

MODELS.PY REQUIREMENTS:
All models must include these specific properties that will be used in templates:

Member model:

- full_name property (returns f"{first_name} {last_name}")
- age property (calculated from date_of_birth)

MembershipPlan model:

- price property (for displaying monthly_price with currency)

WorkoutSession model:

- duration_minutes property (for session length display)
- available_spots property (max_capacity - current_bookings)

SAMPLE DATA REQUIREMENTS:
Include realistic sample data with proper relationships:

- 3 Members with different statuses (Active, Inactive, Pending)
- 3 MembershipPlans (Basic, Premium, VIP) with different prices
- 3 Trainers with different specializations
- 3 WorkoutSessions scheduled for next week
- MemberPlan assignments connecting members to plans
- SessionBooking records showing member session registrations

TESTING VERIFICATION:
After implementation, these URLs should work:

- http://localhost:5000/ (dashboard with stats)
- http://localhost:5000/members (members list)
- http://localhost:5000/plans (plans display)
- http://localhost:5000/sessions (sessions list)

DO NOT CREATE /api/ ROUTES - Use standard Flask routes as listed above.

````

## ✅ **POST-DEVELOPMENT VERIFICATION**

**CRITICAL: Test these exact URLs after Copilot completes the backend:**

```powershell
# Activate virtual environment (if not already active)
.venv\Scripts\activate

# Navigate to src and initialize database
Set-Location src
python init_db.py
python app.py
```

**Browser Testing Checklist:**
- ✅ http://localhost:5000/ (dashboard with statistics)
- ✅ http://localhost:5000/members (members list page)
- ✅ http://localhost:5000/plans (membership plans)
- ✅ http://localhost:5000/sessions (workout sessions)

**If any URL returns 404 Not Found:**
- Verify app.py has @app.route('/') decorator (not @app.route('/api/dashboard'))
- Check that config.py uses proper class structure
- Ensure init_db.py runs without errors

## 🛠️ **TROUBLESHOOTING**

**Common Issues and Solutions:**

**"unable to open database file" error:**
- Ensure config.py uses absolute path with `basedir = os.path.abspath(os.path.dirname(__file__))`
- Verify `src\instance\` directory exists
- Check that database URI uses forward slashes: `f'sqlite:///{os.path.join(basedir, "instance", "fitness_club.db")}'`

**404 Not Found for routes:**
- Verify app.py imports: `from models import db, Member, MembershipPlan, ...`
- Check route decorators use exact paths: `@app.route('/')` not `@app.route('/api/dashboard')`
- Ensure Flask app configuration: `app.config.from_object(config)`

**Template errors:**
- Templates will be created in Sprint 2 - expect TemplateNotFound errors for now
- Focus on route functionality and database operations

## 🎯 **EXPECTED DELIVERABLES**

- ✅ Complete database schema with 6 tables and relationships
- ✅ Flask app with 8 working routes (/, /members, /members/create, etc.)
- ✅ Sample data populated via init_db.py
- ✅ Working database operations (no SQLite errors)
- ✅ All URLs returning 200 status (templates will be added in Sprint 2)

## 📚 **QUICK ACCESS TO OTHER PROMPTS**

- [2_Pre-Sprint-Setup.md](2_Pre-Sprint-Setup.md) - 🔧 Setup & Environment
- [4_Sprint2-Frontend.md](4_Sprint2-Frontend.md) - 🎨 Frontend Templates
- [5_Sprint3-Integration.md](5_Sprint3-Integration.md) - 🔗 Integration & Polish
- [45-minute-live-coding-guide.md](45-minute-live-coding-guide.md) - 🎬 Live Demo Guide

## 🎯 **NEXT STEP**

After completing Sprint 1, proceed to: **[4_Sprint2-Frontend.md](4_Sprint2-Frontend.md)** - Frontend Templates
````
