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

## 🧱 Tech Stack

| Layer    | Technology   |
| -------- | ------------ |
| Backend  | Python Flask |
| Frontend | Tailwind CSS |
| Database | SQLite       |

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

## 💡 Copilot Prompt Guide

Start typing comments like:

```python
# Create a Flask app with SQLite connection
# Define a route to display the list of members
# Tailwind CSS layout for the homepage
# HTML form to register new members
# Create the database schema for members and plans
```

Let Copilot help scaffold the code for you!

## ⏱️ Time Challenge

Try to complete all core features in 45 minutes. Break it into three 15-minute sprints:

1. Backend setup + DB schema
2. Frontend forms + templates
3. Integration + polish
