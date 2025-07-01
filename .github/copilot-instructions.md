# 🤖 GitHub Copilot Instructions: Fitness Club Membership System

This project is a **45-minute live coding demo** to build a full-stack Flask app for managing a fitness club. GitHub Copilot Agent should assist by following the structured sprints, file structure, naming conventions, and prompt-driven development flow.

---

## 🧭 General Instructions

- **Language:** Python 3.11+
- **Frameworks:** Flask, SQLAlchemy, Flask-WTF
- **Database:** SQLite (`src/instance/fitness_club.db`)
- **Frontend:** TailwindCSS (CDN, no build)
- **Testing:** Pytest
- **Environment:** `.venv`, configured via `requirements.txt`

---

## 📁 Folder Structure

```
project-root/
│
├── src/
│   ├── app.py
│   ├── config.py
│   ├── init_db.py
│   ├── models.py
│   ├── templates/
│   ├── static/
│   ├── instance/
│
├── tests/
│   └── test_home.py
│
├── docs/
├── requirements.txt
├── .gitignore
├── README.md
└── .github/
    └── copilot-instructions.md
```

---

## 🧱 Sprints & Prompts

### ✅ 1. Pre-Sprint Setup (`2_Pre-Sprint-Setup.md`)

- Set up virtual environment
- Install dependencies
- Create project folder structure
- Scaffold Flask app with welcome home page
- TailwindCSS via CDN

### ✅ 2. Sprint 1 - Backend Foundation (`3_Sprint1-Backend.md`)

- Build 6 SQLAlchemy models
- Create routes for CRUD and dashboard
- Add `init_db.py` with sample data
- Use relationships (foreign keys) where required

### ✅ 3. Sprint 2 - Frontend Templates (`4_Sprint2-Frontend.md`)

- Create templates for member listing, plan details, session schedule
- Extend from a base layout with TailwindCSS
- Integrate Flask-WTF forms
- Add flash messaging and navigation

### ✅ 4. Sprint 3 - Integration & Polish (`5_Sprint3-Integration.md`)

- Add:
  - Form validation (server/client side)
  - CSV export routes
  - AJAX endpoints
  - Booking system with capacity enforcement
  - Error handling & custom error pages
  - Final polish and mobile responsiveness

---

## ✍️ Coding Standards

- Use `camelCase` for variables/functions
- Use `PascalCase` for classes/models
- Use `ALL_CAPS` for constants
- Private members prefixed with `_`
- Use `try/except` for async and DB operations
- Always log contextual error messages
- Organize HTML with semantic TailwindCSS components

---

## 🧪 Validation Commands

```bash
# Activate environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Run app
cd src
python app.py

# Test home page
cd ..
pytest tests/test_home.py -v

# Trigger database
python src/init_db.py

# Access web UI
http://localhost:5000
```

---

## 🤖 Copilot Agent Expectations

- Prefer `cat <<EOF` blocks for script creation
- Assist with:
  - Flask route generation
  - SQLAlchemy model relationships
  - Flask-WTF forms with validation
  - TailwindCSS components
  - Pytest test creation
- Respect prompt files in order (`2_`, `3_`, `4_`, `5_`)
- Suggest code only within scope of sprint prompt

---

## ✅ Completion Criteria

- Working full-stack Flask app with member/session management
- CSV export + AJAX endpoints
- Mobile-ready Tailwind UI
- Clean, tested, modular codebase

---

> 🧠 Tip: Refer to `6_Master-All-Prompts.md` if Copilot loses context or to regenerate prompt sequences.
