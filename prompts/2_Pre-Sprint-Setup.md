# 🚀 Pre-Sprint Setup: Environment & Dependencies

## 🎯 **SETUP PROMPT** (5 minutes before Sprint 1)

```text
Set up the development environment for a Flask fitness club membership system:

REQUIREMENTS:
1. Create virtual environment (.venv)
2. Install Flask dependencies
3. Create basic project structure
4. Set up folder organization

FOLDERS TO CREATE:
- src/ (main application code)
- src/templates/ (HTML templates)
- src/static/ (CSS, JS, images)
- src/instance/ (database files)
- tests/ (test files)
- docs/ (documentation)

DEPENDENCIES TO INSTALL:
- Flask==3.0.0
- Flask-SQLAlchemy==3.1.1
- Werkzeug==3.0.1

Create requirements.txt with these dependencies and set up virtual environment.
```

## ✅ **SETUP COMMANDS**

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Create requirements.txt
echo "Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1" > requirements.txt

# Install dependencies
pip install -r requirements.txt

# Create folder structure
mkdir src tests docs
mkdir src\templates src\static src\instance
```

## 🎯 **EXPECTED DELIVERABLES**

- ✅ Virtual environment activated
- ✅ Dependencies installed
- ✅ Folder structure created
- ✅ Ready for Sprint 1 development

**Time**: 5 minutes
**Next**: Sprint 1 - Backend Foundation
