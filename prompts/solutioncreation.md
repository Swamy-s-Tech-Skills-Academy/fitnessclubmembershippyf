# 🏋️‍♀️ Fitness Club Membership Full Project

Welcome to the Fitness Club Membership Full Project! This comprehensive full-stack project helps students build a production-ready membership management system using **Python Flask**, **Tailwind CSS**, and **SQLite** — designed for rapid development and learning.

## 🎯 Learning Objectives

By completing this project, you will:

- Master CRUD operations with Flask and SQLite
- Build responsive UIs with Tailwind CSS
- Implement form validation and error handling
- Structure a full-stack web application
- Practice database design and relationships
- Deploy a working web application

## 🚀 Project Goal

Build a lightweight, full-stack web application to:

- Register members and manage their profiles
- Choose and assign membership plans
- Schedule and track workout sessions

The goal is to help students practice CRUD operations, basic layout structuring with Tailwind, and working with a local SQLite database.

## 🛠️ Tech Stack

| Layer    | Technology   |
| -------- | ------------ |
| Backend  | Python Flask |
| Frontend | Tailwind CSS |
| Database | SQLite       |

## 📋 Pre-Sprint Setup (Essential First Steps)

Before starting any sprint, complete these foundational steps:

### 🚀 Step 1: Environment Setup

1. **Verify Python Installation**

   ```bash
   python --version  # Should be Python 3.8+ (3.12.5 recommended)
   ```

2. **Create Virtual Environment**

   ```bash
   # Navigate to project root
   cd fitness-club-membership

   # Create virtual environment
   python -m venv .venv
   ```

3. **Activate Virtual Environment**

   ```bash
   # Windows (PowerShell/CMD)
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 🗂️ Step 2: Project Structure Verification

Ensure your project has this structure:

```text
fitness-club-membership/           # PROJECT ROOT
├── README.md                     # Documentation
├── requirements.txt              # Dependencies (ROOT LEVEL)
├── .venv/                        # Virtual environment
├──
├── src/                          # SOURCE CODE
│   ├── app.py                   # Flask application
│   ├── models.py                # Database models
│   ├── config.py                # Configuration
│   ├── init_db.py               # DB initialization
│   ├── templates/               # HTML templates
│   ├── static/                  # CSS/JS/Images
│   └── instance/                # SQLite database
├──
├── tests/                       # TESTS (parallel to src)
│   ├── conftest.py             # Test configuration
│   ├── test_sprint1.py         # Sprint tests
│   └── manual_test_sprint1.py  # Manual tests
└──
└── docs/                       # Additional documentation
```

### 🧪 Step 3: Pre-Sprint Validation

Run these checks before starting any sprint:

1. **Database Initialization**

   ```bash
   cd src
   python init_db.py
   ```

2. **Sprint Testing**

   ```bash
   # From project root
   cd tests
   python manual_test_sprint1.py
   ```

3. **Flask App Quick Check**
   ```bash
   cd src
   python app.py
   # Should start server on http://localhost:5000
   ```

### ✅ Pre-Sprint Checklist

- [ ] Virtual environment created and activated
- [ ] Dependencies installed successfully
- [ ] Project structure matches template
- [ ] Database initialized with sample data
- [ ] Flask app starts without errors
- [ ] Tests run successfully
- [ ] Port 5000 available for development

### 🔧 Troubleshooting Common Issues

**Import Errors:**

- Ensure virtual environment is activated
- Check that you're in the correct directory
- Verify all dependencies are installed

**Database Errors:**

- Delete `instance/fitness_club.db` and re-run `init_db.py`
- Check file permissions in project directory

**Port Conflicts:**

- Change port in `app.py`: `app.run(port=5001)`
- Kill existing processes using port 5000

### 📊 Success Criteria

Pre-Sprint setup is complete when:

- ✅ Virtual environment shows in terminal prompt
- ✅ `pip list` shows Flask and dependencies
- ✅ Database contains sample members and plans
- ✅ Flask app homepage loads at localhost:5000
- ✅ No import or module errors
- ✅ Tests pass without failures

## ⚙️ Core Features to Implement

### 👥 Member Management

- [ ] **Member Registration**: Name, Age, Gender, Email, Phone, Emergency Contact
- [ ] **Member Profile**: View and edit member details
- [ ] **Member List**: Search, filter, and paginate members
- [ ] **Member Status**: Active, Inactive, Suspended

### 📋 Membership Plans

- [ ] **Plan Types**: Basic ($29/month), Pro ($49/month), Elite ($79/month)
- [ ] **Plan Features**: Gym access, classes, personal training sessions
- [ ] **Plan Assignment**: Assign and change member plans
- [ ] **Billing Cycle**: Monthly, Quarterly, Annual options

### 🗓️ Workout Session Management

- [ ] **Session Scheduler**: Book sessions by day, time, and trainer
- [ ] **Trainer Management**: Add trainers with specializations
- [ ] **Class Types**: Yoga, CrossFit, Cardio, Strength Training
- [ ] **Capacity Limits**: Maximum participants per session
- [ ] **Session History**: Track completed workouts

### 🎨 User Interface

- [ ] **Responsive Design**: Mobile-first Tailwind CSS layout
- [ ] **Navigation**: Clean, intuitive menu system
- [ ] **Forms**: Validation with error messages
- [ ] **Dashboard**: Overview of members, sessions, and plans

## 📝 Bonus

If time permits:

- [ ] Add route authentication (optional)
- [ ] Export member list to CSV

## 🧠 Detailed File Structure

```text
/fitness-club-membership/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── config.py                      # Configuration settings
├── database.py                    # Database models and setup
├──
├── templates/
│   ├── base.html                  # Base template with Tailwind
│   ├── index.html                 # Homepage/Dashboard
│   ├── members/
│   │   ├── list.html             # Member list view
│   │   ├── detail.html           # Member profile view
│   │   ├── create.html           # Member registration form
│   │   └── edit.html             # Edit member form
│   ├── plans/
│   │   ├── list.html             # Membership plans
│   │   └── assign.html           # Assign plan to member
│   └── sessions/
│       ├── schedule.html         # Session scheduler
│       ├── list.html             # Session list
│       └── book.html             # Book session form
├──
├── static/
│   ├── css/
│   │   └── styles.css            # Custom CSS (minimal)
│   ├── js/
│   │   └── main.js               # JavaScript functionality
│   └── images/
│       └── logo.png              # Club logo
├──
├── fitness_club.db               # SQLite database
└── README.md                     # Project documentation
```

## �️ Database Schema

```sql
-- Members Table
CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    gender VARCHAR(10),
    emergency_contact VARCHAR(100),
    emergency_phone VARCHAR(20),
    join_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Membership Plans Table
CREATE TABLE membership_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    monthly_price DECIMAL(10,2) NOT NULL,
    benefits TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Member Plans (Junction Table)
CREATE TABLE member_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'active',
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (plan_id) REFERENCES membership_plans(id)
);

-- Trainers Table
CREATE TABLE trainers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Workout Sessions Table
CREATE TABLE workout_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    trainer_id INTEGER,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_capacity INTEGER DEFAULT 10,
    current_bookings INTEGER DEFAULT 0,
    FOREIGN KEY (trainer_id) REFERENCES trainers(id)
);

-- Session Bookings Table
CREATE TABLE session_bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'confirmed',
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (session_id) REFERENCES workout_sessions(id)
);
```

## 📋 Sample Data

```sql
-- Insert sample membership plans
INSERT INTO membership_plans (name, description, monthly_price, benefits) VALUES
('Basic', 'Access to gym equipment', 29.99, 'Gym access, Locker room'),
('Pro', 'Gym + Group classes', 49.99, 'Gym access, Group classes, Locker room'),
('Elite', 'Full access + Personal training', 79.99, 'All Pro benefits + 2 personal training sessions/month');

-- Insert sample trainers
INSERT INTO trainers (name, specialization, email, phone) VALUES
('Sarah Johnson', 'Yoga & Pilates', 'sarah@fitclub.com', '555-0101'),
('Mike Torres', 'Strength Training', 'mike@fitclub.com', '555-0102'),
('Emma Davis', 'Cardio & HIIT', 'emma@fitclub.com', '555-0103');
```

## 💡 Advanced Copilot Prompt Guide

Start with these detailed comments to let Copilot build the application:

```python
# Create a Flask app with SQLite connection and proper error handling
# Define database models using SQLAlchemy or raw SQL
# Create a route to display member dashboard with statistics
# Implement member registration with form validation
# Add pagination to member list with search functionality
# Create membership plan assignment with pricing logic
# Build workout session scheduler with capacity management
# Add responsive Tailwind CSS layouts with dark mode support
# Implement AJAX form submissions for better UX
# Add CSV export functionality for member data
```

## ⏱️ Development Timeline

### 🚀 Quick Start (45 minutes)

For rapid prototyping, break into three 15-minute sprints:

1. **Sprint 1**: Backend setup + Basic CRUD
2. **Sprint 2**: Frontend templates + Forms
3. **Sprint 3**: Integration + Styling

### 📈 Full Development (2-4 hours)

For a production-ready application:

**Phase 1: Foundation (45 min)**

- [ ] Project setup and dependencies
- [ ] Database schema creation
- [ ] Basic Flask app structure
- [ ] First route and template

**Phase 2: Core Features (90 min)**

- [ ] Member CRUD operations
- [ ] Membership plan management
- [ ] Basic session scheduling
- [ ] Form validation

**Phase 3: Enhanced UI (60 min)**

- [ ] Tailwind CSS styling
- [ ] Responsive design
- [ ] Navigation and layout
- [ ] Error handling and messages

**Phase 4: Advanced Features (45 min)**

- [ ] Search and filtering
- [ ] Dashboard with statistics
- [ ] Session booking system
- [ ] CSV export functionality

## 🎯 Success Metrics

Your project is ready when you can:

- ✅ Register a new member with validation
- ✅ Assign membership plans to members
- ✅ Schedule and book workout sessions
- ✅ View member list with search/filter
- ✅ Export member data to CSV
- ✅ Navigate the app on mobile devices
