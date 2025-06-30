#!/usr/bin/env python3
"""
Simple Test Execution Script
Runs tests with proper path configuration for src/ folder imports
"""
import sys
import os
import subprocess
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
tests_path = project_root / "tests"

# Add src to Python path
sys.path.insert(0, str(src_path))


def run_individual_tests():
    """Run individual test files to validate each component"""
    print("🧪 Running Individual Test Files")
    print("=" * 50)

    # Test files to run
    test_files = [
        "test_live_coding_validation.py",
        "test_complete_system.py"
    ]

    os.chdir(str(tests_path))

    for test_file in test_files:
        print(f"\n📋 Running {test_file}...")
        try:
            # Run the test file directly with python
            result = subprocess.run([
                sys.executable, test_file
            ], capture_output=True, text=True, cwd=str(tests_path))

            if result.returncode == 0:
                print(f"✅ {test_file} - PASSED")
                if result.stdout:
                    print(f"Output: {result.stdout}")
            else:
                print(f"❌ {test_file} - FAILED")
                if result.stderr:
                    print(f"Error: {result.stderr}")
                if result.stdout:
                    print(f"Output: {result.stdout}")

        except Exception as e:
            print(f"❌ {test_file} - ERROR: {e}")


def run_pytest():
    """Try to run with pytest if available"""
    print("\n🧪 Attempting to run with pytest...")
    try:
        os.chdir(str(tests_path))
        result = subprocess.run([
            sys.executable, "-m", "pytest", "-v", "test_complete_system.py"
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Pytest - PASSED")
            print(result.stdout)
        else:
            print("❌ Pytest - FAILED")
            print(result.stderr)
            print(result.stdout)

    except Exception as e:
        print(f"❌ Pytest not available or failed: {e}")


def validate_application():
    """Quick application validation"""
    print("\n🎯 Quick Application Validation")
    print("=" * 30)

    try:
        # Import and check basic functionality
        from models import Member, MembershipPlan, Trainer, WorkoutSession
        from app import app

        with app.app_context():
            print("✅ Flask app imports successfully")
            print("✅ Models import successfully")
            print("✅ Application context works")

        # Test basic route access
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("✅ Homepage route works")
            else:
                print(f"❌ Homepage route failed: {response.status_code}")

            response = client.get('/members')
            if response.status_code == 200:
                print("✅ Members route works")
            else:
                print(f"❌ Members route failed: {response.status_code}")

    except Exception as e:
        print(f"❌ Application validation failed: {e}")


if __name__ == "__main__":
    print("🎬 Fitness Club Membership System - Test Suite")
    print("=" * 60)
    print(f"Project Root: {project_root}")
    print(f"Source Path: {src_path}")
    print(f"Tests Path: {tests_path}")
    print()

    # Run validation
    validate_application()

    # Run individual tests
    run_individual_tests()

    # Try pytest
    run_pytest()

    print("\n🎉 Test execution completed!")
