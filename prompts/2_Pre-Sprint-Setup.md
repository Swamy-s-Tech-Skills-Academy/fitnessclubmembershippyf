# 🚀 Pre-Sprint Setup: Environment & Dependencies

## 🎯 **SETUP PROMPT** (5 minutes before Sprint 1)

```text
Set up the development environment for a Flask fitness club membership system:

REQUIREMENTS:
1. Create virtual environment (.venv)
2. Install Flask dependencies
3. Create basic project structure
4. Set up folder organization
5. Create basic Flask app with welcome home page

FOLDERS TO CREATE:
- src/ (main application code)
- src/templates/ (HTML templates)
- src/static/ (CSS, JS, images)
- src/instance/ (database files)
- tests/ (test files)
- docs/ (documentation)

DEPENDENCIES TO INSTALL (from requirements.txt):

Core Flask Framework:
- Flask==3.0.0
- Flask-SQLAlchemy==3.1.1
- Flask-WTF==1.2.1

Forms & Validation:
- WTForms==3.1.1
- email-validator==2.1.0

Database & Core Dependencies:
- SQLAlchemy==2.0.23
- Werkzeug==3.0.1
- Jinja2==3.1.2
- MarkupSafe==2.1.3
- click==8.1.7
- itsdangerous==2.1.2
- blinker==1.6.3

Development & Testing:
- pytest==7.4.3
- pytest-flask==1.3.0
- requests==2.31.0

Optional Production/Development:
- gunicorn==21.2.0
- python-dotenv==1.0.0

FRONTEND STYLING:
- TailwindCSS via CDN (no installation required)
- CDN URL: https://cdn.tailwindcss.com

Create requirements.txt with these dependencies and set up virtual environment.
```

## ✅ **SETUP COMMANDS**

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies from existing requirements.txt
pip install -r requirements.txt

# Create folder structure
mkdir src tests docs
mkdir src\templates src\static src\instance
```

## 🏠 **CREATE BASIC WELCOME HOME PAGE**

```bash
# Create basic Flask app (src/app.py) using cat for better formatting
cat <<EOF > src/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
EOF

# Create welcome template (src/templates/index.html)
cat <<EOF > src/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fitness Club Membership System</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center">
    <div class="text-center">
        <h1 class="text-6xl font-bold text-blue-600 mb-4">Welcome to Fitness Club</h1>
        <p class="text-xl text-gray-600">Your fitness journey starts here!</p>
        <div class="mt-8">
            <span class="inline-block bg-green-100 text-green-800 px-4 py-2 rounded-full text-sm font-medium">
                ✅ Flask App Running Successfully
            </span>
        </div>
    </div>
</body>
</html>
EOF

# Create .gitignore for clean repository
cat <<EOF > .gitignore
.venv/
__pycache__/
*.pyc
instance/
.env
*.db
.pytest_cache/
EOF

# Create test placeholder for validation
cat <<EOF > tests/test_home.py
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Fitness Club" in response.data
EOF
```

## 📋 **ALTERNATIVE: Create requirements.txt from scratch**

```bash
# If requirements.txt doesn't exist, create it:
cat <<EOF > requirements.txt
# Fitness Club Membership System - Python Dependencies

# Core Flask Framework
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1

# Forms & Validation
WTForms==3.1.1
email-validator==2.1.0

# Database
SQLAlchemy==2.0.23

# Web Server & Core Dependencies
Werkzeug==3.0.1
Jinja2==3.1.2
MarkupSafe==2.1.3
click==8.1.7
itsdangerous==2.1.2
blinker==1.6.3

# Development & Testing
pytest==7.4.3
pytest-flask==1.3.0
requests==2.31.0

# Optional: Production Deployment
gunicorn==21.2.0

# Optional: Development Tools
python-dotenv==1.0.0
EOF
```

## 🎨 **TAILWINDCSS SETUP**

**No Installation Required!** - Using CDN approach for rapid development:

```html
<!-- Add this to your base.html template <head> section -->
<script src="https://cdn.tailwindcss.com"></script>
```

**Benefits of CDN approach:**

- ✅ No build process required
- ✅ Instant setup for rapid prototyping
- ✅ Perfect for live coding demonstrations
- ✅ All Tailwind classes available immediately

**Note:** For production deployment, consider using Tailwind CLI for optimized builds.

## 🎯 **EXPECTED DELIVERABLES**

- ✅ Virtual environment activated
- ✅ All dependencies installed from requirements.txt
- ✅ Folder structure created (src/, tests/, docs/, templates/, static/, instance/)
- ✅ Basic Flask app created (src/app.py)
- ✅ Welcome home page template created (src/templates/index.html)
- ✅ .gitignore file created for clean repository
- ✅ Test file created (tests/test_home.py) for validation
- ✅ TailwindCSS CDN ready for use in templates
- ✅ Working Flask app with "Welcome to Fitness Club" H1
- ✅ Ready for Sprint 1 development

**Time**: 5 minutes

**Next**: Sprint 1 - Backend Foundation

## 🚀 **TEST YOUR SETUP**

```bash
# Test the basic Flask app
cd src
python app.py
# Visit http://localhost:5000 - you should see "Welcome to Fitness Club"

# Test with pytest (optional validation)
cd ..
pytest tests/test_home.py -v
```

## 🤖 **COPILOT AGENT COMPATIBILITY**

This setup is optimized for Copilot Agent execution:

- ✅ Uses `cat <<EOF` for better multiline file creation
- ✅ Scriptable commands with clear separation
- ✅ Includes .gitignore for clean repository
- ✅ Test validation included
- ✅ No ambiguous shell syntax

**TailwindCSS Note**: The welcome template already includes TailwindCSS CDN, so you'll see styled content immediately!
