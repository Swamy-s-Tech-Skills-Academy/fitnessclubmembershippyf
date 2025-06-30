# 🏗️ Sprint 1: Backend Foundation (15 minutes)

## 🎯 **COPY-PASTE PROMPT FOR SPRINT 1**

```text
Build a complete Flask backend for a fitness club membership system with the following requirements:

MODELS NEEDED:
1. Member (id, first_name, last_name, email, phone, date_of_birth, gender, emergency_contact, emergency_phone, join_date, status)
2. MembershipPlan (id, name, description, monthly_price, benefits)
3. Trainer (id, name, specialization, email, phone)
4. WorkoutSession (id, title, description, trainer_id, session_date, start_time, end_time, max_capacity, current_bookings)
5. MemberPlan (id, member_id, plan_id, start_date, end_date, status)
6. SessionBooking (id, member_id, session_id, booking_date, status)

FILES TO CREATE:
- src/models.py (SQLAlchemy models with relationships)
- src/config.py (Flask configuration)
- src/app.py (Flask app with routes for dashboard, members, plans, sessions)
- src/init_db.py (database initialization with sample data)

ROUTES NEEDED:
- / (dashboard with statistics)
- /members (list with search)
- /members/create (member registration)
- /members/<id> (member details)
- /plans (membership plans)
- /sessions (workout sessions)
- /sessions/schedule (session scheduling)

Include comprehensive sample data: 3 members, 3 plans, 3 trainers, 3 sessions with proper relationships.
Use SQLite database in src/instance/fitness_club.db
```

## ✅ **VALIDATION COMMANDS**

```bash
# Activate virtual environment
.venv\Scripts\activate
cd src
python init_db.py
python app.py
# Visit http://localhost:5000 - should show dashboard
```

## 🎯 **EXPECTED DELIVERABLES**

- ✅ Complete database schema with 6 tables
- ✅ Flask app with 7+ routes
- ✅ Sample data with relationships
- ✅ Working API endpoints
- ✅ Database file created and populated
