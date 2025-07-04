# 🚀 Pre-Sprint Setup: Environment & Dependencies

## 🎯 **COPY-PASTE PROMPT FOR PRE-SPRINT**

```text
Set up the development environment for a Flask fitness club membership system:

PYTHON VERSION REQUIREMENT:
✅ Python 3.13.5 - Required for optimal compatibility with Flask 3.0.0 and SQLAlchemy 2.0.23

STARTER PROJECT INCLUDES:
✅ requirements.txt - All Python dependencies with specific versions
✅ .gitignore - Python/Flask optimized ignore rules
✅ .copilot/settings.json - GitHub Copilot configuration
✅ .github/copilot-instructions.md - Copilot Agent instructions
✅ docs/ folder - Documentation and images (includes favicon.ico)
✅ prompts/ folder - All sprint .md files with copy-paste prompts
✅ LICENSE - Project license
✅ README.md - Project documentation
✅ src/ folder - Complete Flask application with professional welcome page

SETUP TASKS:
1. Create virtual environment (.venv)
2. Install dependencies from provided requirements.txt
3. Verify src/ folder structure (already included)
4. Test the included Flask app with welcome page

INCLUDED FLASK APPLICATION:
- src\app.py (Flask app with template rendering)
- src\templates\index.html (Professional welcome page with TailwindCSS, Font Awesome, Google Fonts)
- src\static\ (Ready for CSS and JS files)
- src\instance\ (Ready for database files)

FAVICON SETUP:
- docs\icons\favicon.ico (Professional fitness-themed favicon)
- Needs to be copied to src\static\favicon.ico during setup
- Will be referenced in HTML templates for browser tab icon

DEPENDENCIES (already defined in requirements.txt):

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

Optional Production/Development:
- gunicorn==21.2.0
- python-dotenv==1.0.0

FRONTEND STYLING:
- TailwindCSS via CDN (no installation required)
- CDN URL: https://cdn.tailwindcss.com
- Font Awesome via CDN (icons and graphics)
- CDN URL: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css
- Google Fonts (Inter & Poppins)
- CDN URL: https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap

✅ All configuration files are included in the starter project - no manual creation needed!
```

## 🏠 **CREATE BASIC WELCOME HOME PAGE**

### **PowerShell File Creation Commands:**

```powershell
# ✅ Copy favicon to static folder (must be done first)
Copy-Item "docs\icons\favicon.ico" -Destination "src\static\favicon.ico" -Force
Write-Host "✅ Favicon copied to src\static\" -ForegroundColor Green

# ✅ Create basic Flask app (src\app.py)
@"
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
"@ | Out-File -FilePath "src\app.py" -Encoding UTF8

# ✅ Create welcome template (src\templates\index.html)
@"
<!DOCTYPE html>
<html lang=`"en`">
<head>
    <meta charset=`"UTF-8`">
    <meta name=`"viewport`" content=`"width=device-width, initial-scale=1.0`">
    <title>Fitness Club Membership System</title>
    <!-- Favicon -->
    <link rel=`"icon`" type=`"image/x-icon`" href=`"{{ url_for('static', filename='favicon.ico') }}`">
    <link rel=`"shortcut icon`" type=`"image/x-icon`" href=`"{{ url_for('static', filename='favicon.ico') }}`">
    <!-- TailwindCSS CDN -->
    <script src=`"https://cdn.tailwindcss.com`"></script>
    <!-- Font Awesome CDN -->
    <link rel=`"stylesheet`" href=`"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css`">
    <!-- Google Fonts -->
    <link href=`"https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap`" rel=`"stylesheet`">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .font-poppins { font-family: 'Poppins', sans-serif; }
    </style>
</head>
<body class=`"bg-gray-100 min-h-screen flex items-center justify-center`">
    <div class=`"text-center`">
        <div class=`"mb-6`">
            <i class=`"fas fa-dumbbell text-6xl text-blue-600 mb-4`"></i>
        </div>
        <h1 class=`"text-6xl font-bold text-blue-600 mb-4 font-poppins`">Welcome to Fitness Club</h1>
        <p class=`"text-xl text-gray-600 mb-6`">Your fitness journey starts here!</p>
        <div class=`"flex justify-center gap-4 mb-8`">
            <div class=`"flex items-center gap-2 text-gray-700`">
                <i class=`"fas fa-users text-blue-500`"></i>
                <span>Members</span>
            </div>
            <div class=`"flex items-center gap-2 text-gray-700`">
                <i class=`"fas fa-calendar-alt text-green-500`"></i>
                <span>Bookings</span>
            </div>
            <div class=`"flex items-center gap-2 text-gray-700`">
                <i class=`"fas fa-chart-line text-purple-500`"></i>
                <span>Analytics</span>
            </div>
        </div>
        <div class=`"mt-8`">
            <span class=`"inline-block bg-green-100 text-green-800 px-4 py-2 rounded-full text-sm font-medium`">
                <i class=`"fas fa-check-circle mr-2`"></i>Flask App Running Successfully
            </span>
        </div>
    </div>
</body>
</html>
"@ | Out-File -FilePath "src\templates\index.html" -Encoding UTF8
```

## 🎨 **FRONTEND STYLING SETUP**

**No Installation Required!** - Using CDN approach for rapid development:

```html
<!-- Add these to your base.html template <head> section -->

<!-- TailwindCSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Font Awesome CDN -->
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
/>

<!-- Google Fonts -->
<link
  href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap"
  rel="stylesheet"
/>
```

**Benefits of CDN approach:**

- ✅ No build process required
- ✅ Instant setup for rapid prototyping
- ✅ Perfect for live coding demonstrations
- ✅ All styling resources available immediately
- ✅ Professional typography with Google Fonts
- ✅ Rich icon library with Font Awesome

**Available Resources:**

- **TailwindCSS**: Complete utility-first CSS framework
- **Font Awesome**: 1,000+ icons for UI elements
- **Inter Font**: Clean, readable body text
- **Poppins Font**: Modern headings and display text

**Note:** For production deployment, consider using build tools for optimized assets.

## 🎯 **EXPECTED DELIVERABLES**

- ✅ Virtual environment created and activated
- ✅ All Flask dependencies installed (Flask, SQLAlchemy, Flask-WTF, etc.)
- ✅ Project folder structure verified (src\, templates\, static\, instance\)
- ✅ Professional Flask app tested with welcome page
- ✅ Favicon properly configured and displaying in browser tab
- ✅ CDN resources verified (Tailwind CSS, Font Awesome, Google Fonts loading correctly)
- ✅ HTTP responses working and professional styling visible

## 🧪 **PRE-SPRINT VERIFICATION CHECKLIST**

**Manual verification steps for the user to confirm setup is working:**

### **🔍 Step 1: Smart Virtual Environment Setup**

```powershell
# Navigate to your project root directory
Set-Location "path\to\your\project"

# Verify Python version first
$pythonVersion = python --version
Write-Host "🐍 Python Version: $pythonVersion" -ForegroundColor Cyan
if ($pythonVersion -notmatch "3\.13\.5") {
    Write-Host "⚠️  Recommended Python version is 3.13.5 for optimal compatibility" -ForegroundColor Yellow
}

# Smart detection and setup of virtual environment
if (Test-Path ".venv") {
    Write-Host "✅ Virtual environment already exists" -ForegroundColor Green
    Write-Host "🔄 Activating existing environment..." -ForegroundColor Yellow
    .venv\Scripts\activate

    # Verify Flask installation and version
    $flaskCheck = pip list | Select-String -Pattern "Flask==3.0.0"
    if (-not $flaskCheck) {
        Write-Host "⚠️  Flask version mismatch or missing. Updating dependencies..." -ForegroundColor Yellow
        pip install -r requirements.txt
        Write-Host "✅ Dependencies updated successfully" -ForegroundColor Green
    } else {
        Write-Host "✅ Dependencies are up to date" -ForegroundColor Green
    }
} else {
    Write-Host "🆕 Creating new virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green

    Write-Host "🔄 Activating virtual environment..." -ForegroundColor Yellow
    .venv\Scripts\activate

    Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "✅ All dependencies installed successfully" -ForegroundColor Green
}

# Verify you see (.venv) in your prompt
Write-Host "🎯 Virtual environment setup complete!" -ForegroundColor Green
```

### **Step 2: Create Project Structure**

```powershell
# Create necessary directories if they don't exist
$directories = @("src", "src\templates", "src\static", "src\instance")
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "✅ Created directory: $dir" -ForegroundColor Green
    } else {
        Write-Host "✅ Directory already exists: $dir" -ForegroundColor Gray
    }
}

# Copy favicon to static folder if it doesn't exist
if (-not (Test-Path "src\static\favicon.ico")) {
    if (Test-Path "docs\icons\favicon.ico") {
        Copy-Item "docs\icons\favicon.ico" -Destination "src\static\favicon.ico" -Force
        Write-Host "✅ Favicon copied to src\static\" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Favicon not found in docs\icons\" -ForegroundColor Yellow
    }
} else {
    Write-Host "✅ Favicon already exists in src\static\" -ForegroundColor Gray
}
```

### **Step 3: Verify Dependencies**

```powershell
# Check Flask installation
pip list | Select-String -Pattern "Flask"
# Expected: Flask==3.0.0, Flask-SQLAlchemy==3.1.1, Flask-WTF==1.2.1

# Quick dependency verification
pip list | Select-String -Pattern "SQLAlchemy|WTForms|Jinja2"
```

### **Step 4: Test Basic Flask Setup**

Test the existing Flask app (already included in starter project):

```powershell
# Navigate to src folder and test the Flask app
Set-Location src
python app.py
```

### **Step 5: Manual Browser Verification**

- Open browser to `http://127.0.0.1:5000`
- Verify you see: **"Welcome to Fitness Club"** with professional styling
- Confirm TailwindCSS, Font Awesome icons, and Google Fonts are loading
- **Check favicon appears in browser tab** (fitness-themed icon)
- Stop the server with `Ctrl+C`
- Return to project root: `Set-Location ..`

### **Step 6: Final Completion Check**

```powershell
# Simple completion validation
python -c "print('🎯 PRE-SPRINT COMPLETION CHECK'); print('=' * 40); print('✅ Virtual Environment: Active'); print('✅ Flask App: Running'); print('✅ Dependencies: Installed'); print('✅ Project Structure: Complete'); print('=' * 40); print('🚀 READY FOR SPRINT 1!')"
```

---

**✅ ALL CHECKS PASSED?** → **Ready for Sprint 1!**  
**❌ ANY FAILURES?** → **Review setup steps and fix issues**

---

## 🚀 **PRE-SPRINT SETUP COMPLETE**

Once all verification steps pass, you're ready to proceed with:

- **Sprint 1:** [3_Sprint1-Backend.md](3_Sprint1-Backend.md) - Backend Development
- **Live Demo Guide:** [45-minute-live-coding-guide.md](45-minute-live-coding-guide.md) - Complete presentation guide

## 🤖 **COPILOT AGENT COMPATIBILITY**

This setup is optimized for Copilot Agent execution on Windows:

- ✅ Uses PowerShell `@"..."@` syntax for better multiline file creation
- ✅ Windows-specific PowerShell commands and color output
- ✅ Smart virtual environment detection and handling
- ✅ Scriptable commands with Windows path separators (\)
- ✅ .gitignore already included in starter project
- ✅ Copilot configuration already included in starter project
- ✅ Development-focused workflow optimized for Windows 11

## 💡 **IMPORTANT NOTES FOR SPRINT 1**

**Terminal Navigation:** Always use `Set-Location src` before running Flask commands. New terminals start in the project root, not the src folder.

**Database Configuration:** The `src\instance\` folder is crucial for Sprint 1 database initialization. Sprint 1 will use absolute paths to prevent "unable to open database file" errors.

**Environment Persistence:** The smart .venv detection ensures consistent results across multiple demo runs and workshop scenarios.

**Pre-built Application:** The starter includes a complete Flask app with professional styling - no manual file creation needed!

## 📚 **QUICK ACCESS TO OTHER PROMPTS**

- [3_Sprint1-Backend.md](3_Sprint1-Backend.md) - 🛠 Backend Development
- [4_Sprint2-Frontend.md](4_Sprint2-Frontend.md) - 🎨 Frontend Templates
- [5_Sprint3-Integration.md](5_Sprint3-Integration.md) - 🔗 Integration & Polish
- [45-minute-live-coding-guide.md](45-minute-live-coding-guide.md) - 🎬 Live Demo Guide

**Styling Resources Note**: The test Flask app provides a simple verification. The actual professional styling with TailwindCSS, Font Awesome, and Google Fonts will be implemented in Sprint 2!
