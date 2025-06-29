# 🚀 Pre-Sprint Quick Reference

## Essential Setup Commands (Run Once)

```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
cd src
python init_db.py

# 5. Test setup
cd ../tests
python manual_test_sprint1.py

# 6. Start development server
cd ../src
python app.py
```

## Daily Development Workflow

```bash
# 1. Activate environment (every new terminal session)
.venv\Scripts\activate

# 2. Navigate to appropriate folder
cd src          # For running the app
cd tests        # For running tests

# 3. Run the application
python app.py   # Starts server on localhost:5000

# 4. Run tests (from project root)
python tests/manual_test_sprint1.py
```

## Project Structure Reference

```
fittnessclubmembershippyf/     # Always start here
├── README.md               # Main documentation
├── requirements.txt        # Dependencies (install from here)
├── .venv/                  # Virtual environment
├── src/                   # Source code (run app.py from here)
├── tests/                 # Tests (run tests from here)
└── docs/                  # Documentation
```

## Troubleshooting

**Virtual Environment Issues:**

- Ensure you're in project root when creating venv
- Always activate before installing packages
- Look for `(.venv)` in terminal prompt

**Import Errors:**

- Check you're in correct directory (src/ for app, tests/ for tests)
- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`

**Database Issues:**

- Delete `src/instance/fitness_club.db` and re-run `init_db.py`
- Check file permissions

**Port 5000 in Use:**

- Change port in app.py: `app.run(port=5001)`
- Or kill process using port: `netstat -ano | findstr :5000`

## Success Indicators

- ✅ `(.venv)` appears in terminal prompt
- ✅ `pip list` shows Flask and dependencies
- ✅ Database file exists: `src/instance/fitness_club.db`
- ✅ App starts without errors
- ✅ Browser shows dashboard at localhost:5000
- ✅ Tests pass without failures
