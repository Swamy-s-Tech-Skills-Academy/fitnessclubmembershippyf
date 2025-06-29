# 🏋️‍♀️ Fitness Club Membership Starter Project

Welcome to the Fitness Club Membership Starter! This full-stack project helps students build a working membership management system using **Python Flask**, **Tailwind CSS**, and **SQLite** — all in under 45 minutes.

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

## ⚙️ Features to Implement

- [ ] Member Signup Form (Name, Age, Gender, Contact)
- [ ] List & View Member Details
- [ ] Membership Plan Options (Basic, Pro, Elite)
- [ ] Workout Session Scheduler (Day, Time, Trainer)
- [ ] Tailwind-based UI with mobile responsiveness
- [ ] Store everything in SQLite (members, plans, workouts)

## 📝 Bonus

If time permits:

- [ ] Add route authentication (optional)
- [ ] Export member list to CSV

## 🧠 Suggested File Structure

```text

/fitness-club
├── app.py
├── templates/
│ ├── base.html
│ ├── index.html
│ └── member.html
├── static/
│ └── styles.css
├── db.sqlite3
└── README.md
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
