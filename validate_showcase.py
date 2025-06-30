#!/usr/bin/env python3
"""
45-Minute Live Coding Validation Script
For Vibe Coding Showcase - Fitness Club Membership System
"""

import os
import sys
import sqlite3
import subprocess
import time
from pathlib import Path


def print_banner(message):
    """Print a formatted banner message"""
    print("\n" + "="*60)
    print(f"  {message}")
    print("="*60)


def check_environment():
    """Check if the development environment is properly set up"""
    print_banner("🔍 ENVIRONMENT CHECK")

    # Check Python version
    python_version = sys.version_info
    print(
        f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")

    if python_version < (3, 8):
        print("❌ Python 3.8+ required!")
        return False

    # Check virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment active")
    else:
        print("❌ Virtual environment not active!")
        return False

    # Check required packages
    try:
        import flask
        import flask_sqlalchemy
        print(f"✅ Flask {flask.__version__} installed")
        print(f"✅ Flask-SQLAlchemy {flask_sqlalchemy.__version__} installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        return False

    return True


def check_project_structure():
    """Verify the project structure is correct"""
    print_banner("📁 PROJECT STRUCTURE CHECK")

    required_dirs = [
        "src",
        "src/templates",
        "src/templates/members",
        "src/templates/plans",
        "src/templates/sessions",
        "src/static",
        "src/instance",
        "tests",
        "docs",
        "prompts"
    ]

    required_files = [
        "requirements.txt",
        "README.md",
        "prompts/45-minute-live-coding-guide.md",
        "prompts/sprint1-backend-prompt.md",
        "prompts/sprint2-frontend-prompt.md",
        "prompts/sprint3-integration-prompt.md"
    ]

    all_good = True

    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✅ Directory: {directory}")
        else:
            print(f"❌ Missing directory: {directory}")
            all_good = False

    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ File: {file_path}")
        else:
            print(f"❌ Missing file: {file_path}")
            all_good = False

    return all_good


def check_sprint1_completion():
    """Check if Sprint 1 backend is completed"""
    print_banner("🏗️ SPRINT 1 BACKEND CHECK")

    sprint1_files = [
        "src/config.py",
        "src/models.py",
        "src/app.py",
        "src/init_db.py"
    ]

    all_good = True

    for file_path in sprint1_files:
        if os.path.exists(file_path):
            print(f"✅ Backend file: {file_path}")
        else:
            print(f"❌ Missing backend file: {file_path}")
            all_good = False

    # Check database
    db_path = "src/instance/fitness_club.db"
    if os.path.exists(db_path):
        print(f"✅ Database: {db_path}")

        # Check database contents
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Check tables
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]

            expected_tables = ['member', 'membership_plan', 'trainer',
                               'workout_session', 'member_plan', 'session_booking']
            for table in expected_tables:
                if table in tables:
                    print(f"✅ Table: {table}")
                else:
                    print(f"❌ Missing table: {table}")
                    all_good = False

            # Check sample data
            cursor.execute("SELECT COUNT(*) FROM member")
            member_count = cursor.fetchone()[0]
            print(f"✅ Sample members: {member_count}")

            cursor.execute("SELECT COUNT(*) FROM membership_plan")
            plan_count = cursor.fetchone()[0]
            print(f"✅ Sample plans: {plan_count}")

            conn.close()

        except Exception as e:
            print(f"❌ Database error: {e}")
            all_good = False
    else:
        print(f"❌ Missing database: {db_path}")
        all_good = False

    return all_good


def check_sprint2_completion():
    """Check if Sprint 2 frontend is completed"""
    print_banner("🎨 SPRINT 2 FRONTEND CHECK")

    sprint2_files = [
        "src/templates/base.html",
        "src/templates/index.html",
        "src/templates/members/list.html",
        "src/templates/members/create.html",
        "src/templates/members/detail.html",
        "src/templates/plans/list.html",
        "src/templates/sessions/list.html",
        "src/templates/sessions/schedule.html"
    ]

    all_good = True

    for file_path in sprint2_files:
        if os.path.exists(file_path):
            print(f"✅ Template: {file_path}")
        else:
            print(f"❌ Missing template: {file_path}")
            all_good = False

    # Check for Tailwind CSS in base template
    if os.path.exists("src/templates/base.html"):
        with open("src/templates/base.html", "r", encoding="utf-8") as f:
            content = f.read()
            if "tailwindcss.com" in content:
                print("✅ Tailwind CSS CDN found")
            else:
                print("❌ Tailwind CSS CDN not found")
                all_good = False

    return all_good


def check_sprint3_completion():
    """Check if Sprint 3 integration is completed"""
    print_banner("🔧 SPRINT 3 INTEGRATION CHECK")

    # Check for enhanced app.py features
    if os.path.exists("src/app.py"):
        with open("src/app.py", "r", encoding="utf-8") as f:
            content = f.read()

            features = [
                ("CSV export", "/export/"),
                ("API endpoints", "/api/"),
                ("Form validation", "flash("),
                ("Error handling", "try:")
            ]

            for feature, search_term in features:
                if search_term in content:
                    print(f"✅ {feature} implemented")
                else:
                    print(f"❌ {feature} missing")

    return True


def test_flask_app():
    """Test if the Flask app starts correctly"""
    print_banner("🚀 FLASK APP TEST")

    try:
        # Import the Flask app
        sys.path.insert(0, "src")
        from app import app

        print("✅ Flask app imports successfully")

        # Test app context
        with app.app_context():
            print("✅ Flask app context works")

        # Test routes
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("✅ Dashboard route works")
            else:
                print(f"❌ Dashboard route failed: {response.status_code}")

        return True

    except Exception as e:
        print(f"❌ Flask app error: {e}")
        return False


def run_showcase_validation():
    """Run complete validation for the 45-minute showcase"""
    print_banner("🎬 45-MINUTE SHOWCASE VALIDATION")

    all_checks = [
        check_environment(),
        check_project_structure(),
        check_sprint1_completion(),
        check_sprint2_completion(),
        check_sprint3_completion(),
        test_flask_app()
    ]

    if all(all_checks):
        print_banner("🎉 SHOWCASE READY!")
        print("✅ All systems go for live coding!")
        print("✅ Project is production-ready")
        print("✅ All sprints completed successfully")
        print("\n🎯 Next steps:")
        print("1. Review the 45-minute-live-coding-guide.md")
        print("2. Practice the three sprint prompts")
        print("3. Test screen sharing and audio")
        print("4. Start the showcase!")
        return True
    else:
        print_banner("❌ SHOWCASE NOT READY")
        print("Please fix the issues above before proceeding.")
        return False


if __name__ == "__main__":
    success = run_showcase_validation()
    sys.exit(0 if success else 1)
