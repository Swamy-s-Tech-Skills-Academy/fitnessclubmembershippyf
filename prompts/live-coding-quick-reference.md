# 🎬 LIVE CODING QUICK REFERENCE CARD

## ⏰ **45-MINUTE TIMELINE**

| Time      | Sprint   | Focus    | Key Deliverable            |
| --------- | -------- | -------- | -------------------------- |
| 0-15 min  | Sprint 1 | Backend  | 6 models + Flask routes    |
| 15-30 min | Sprint 2 | Frontend | 8 templates + Tailwind     |
| 30-45 min | Sprint 3 | Polish   | Validation + Export + AJAX |

## 🎯 **EXACT PROMPTS TO USE**

### **Sprint 1 Prompt** (Copy exactly):

```
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

### **Sprint 2 Prompt** (Copy exactly):

```
Create a complete responsive frontend for the fitness club system using Tailwind CSS:

TEMPLATES NEEDED:
1. base.html - Navigation with Tailwind, responsive design, footer
2. index.html - Dashboard with 8 key metrics (members, sessions, revenue, growth)
3. members/list.html - Member list with search, filters, export button
4. members/create.html - Member registration form with validation
5. members/detail.html - Member profile with plan assignment
6. plans/list.html - Membership plans with pricing cards
7. sessions/list.html - Session list with booking functionality
8. sessions/schedule.html - Session scheduling form

FEATURES TO INCLUDE:
- Mobile-responsive navigation with hamburger menu
- Professional Tailwind CSS styling (blue/gray theme)
- Form validation with error messages
- Data tables with hover effects
- Button styling (primary, secondary, danger)
- Card layouts for plans and statistics
- Export functionality (CSV buttons)
- Progress bars for analytics
- Professional footer with contact info

Use CDN for Tailwind: https://cdn.tailwindcss.com
All forms should connect to existing Flask routes
Include proper error handling and success messages
```

### **Sprint 3 Prompt** (Copy exactly):

```
Complete the fitness club system with advanced features and production polish:

ADVANCED FEATURES TO ADD:
1. Form validation (server-side and client-side)
2. CSV export functionality for members and sessions
3. AJAX endpoints for member status toggle and session bookings
4. Enhanced dashboard with revenue calculations and growth metrics
5. Session booking system with capacity management
6. Search and filtering for members and sessions
7. Error handling and user feedback messages
8. Mobile optimization and final polish

SPECIFIC IMPLEMENTATIONS:
- Add CSV export routes (/export/members, /export/sessions)
- Create API endpoints (/api/member/<id>/toggle-status, /api/session/<id>/bookings)
- Enhance app.py with comprehensive validation
- Add JavaScript for AJAX calls and form enhancement
- Implement session booking logic with capacity checking
- Add context processor for navigation highlighting
- Create professional error pages
- Add final styling touches and animations

VALIDATION REQUIREMENTS:
- No duplicate emails for members
- Date validation (no future birth dates)
- Session capacity cannot exceed max_capacity
- Proper error messages for all scenarios
- Success notifications for all actions

The system should be production-ready with all features working smoothly.
```

## 🚀 **PRE-SHOW SETUP COMMANDS**

```bash
mkdir fittnessclubmembershippyf
cd fittnessclubmembershippyf
echo "Flask==3.0.0" > requirements.txt
echo "Flask-SQLAlchemy==3.1.1" >> requirements.txt
echo "Werkzeug==3.0.1" >> requirements.txt
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
mkdir src tests docs prompts
mkdir src\templates src\static src\instance
mkdir src\templates\members src\templates\plans src\templates\sessions
```

## ✅ **VALIDATION COMMANDS**

### After Sprint 1:

```bash
cd src
python init_db.py
python app.py
# Visit http://localhost:5000
```

### After Sprint 2:

```bash
# Check all templates load
# Test responsive design
```

### After Sprint 3:

```bash
# Test all features
# Export CSV files
# Check mobile view
```

## 🎤 **KEY TALKING POINTS**

- **"We're building a complete fitness club management system in 45 minutes"**
- **"Using Python Flask for rapid backend development"**
- **"Tailwind CSS for instant professional styling"**
- **"SQLite for zero-config database"**
- **"Sprint methodology for organized development"**
- **"Production-ready features in minimal time"**

## 🏆 **FINAL DEMO FEATURES**

1. ✅ **Member Registration** - Complete form with validation
2. ✅ **Dashboard Analytics** - 8 key business metrics
3. ✅ **Session Booking** - Capacity management system
4. ✅ **Data Export** - Professional CSV downloads
5. ✅ **Mobile Responsive** - Works on all devices
6. ✅ **Real-time Updates** - AJAX status toggles
7. ✅ **Search & Filter** - Find members and sessions
8. ✅ **Professional UI** - Production-ready design

## 🎯 **SUCCESS METRICS**

By the end of 45 minutes:

- ✅ Complete full-stack application
- ✅ 6 database models with relationships
- ✅ 8 responsive web pages
- ✅ All CRUD operations working
- ✅ CSV export functionality
- ✅ Mobile-responsive design
- ✅ Production-ready features
