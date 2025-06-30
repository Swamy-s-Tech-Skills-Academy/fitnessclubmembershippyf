#!/usr/bin/env python3
"""
Simple test script to validate the fitness club application
"""
import sys
import os
import requests
import json

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_application():
    """Test the running Flask application"""
    print("🧪 Testing Fitness Club Application")
    print("=" * 50)

    base_url = "http://localhost:5000"

    # Test 1: Homepage
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            print("✅ Homepage loads successfully")
        else:
            print(f"❌ Homepage failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Homepage error: {e}")

    # Test 2: Members page
    try:
        response = requests.get(f"{base_url}/members")
        if response.status_code == 200:
            print("✅ Members page loads successfully")
        else:
            print(f"❌ Members page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Members page error: {e}")

    # Test 3: Plans page
    try:
        response = requests.get(f"{base_url}/plans")
        if response.status_code == 200:
            print("✅ Plans page loads successfully")
        else:
            print(f"❌ Plans page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Plans page error: {e}")

    # Test 4: Sessions page
    try:
        response = requests.get(f"{base_url}/sessions")
        if response.status_code == 200:
            print("✅ Sessions page loads successfully")
        else:
            print(f"❌ Sessions page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Sessions page error: {e}")

    # Test 5: Member creation page
    try:
        response = requests.get(f"{base_url}/members/create")
        if response.status_code == 200:
            print("✅ Member creation page loads successfully")
        else:
            print(f"❌ Member creation page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Member creation page error: {e}")

    print("\n🎯 Basic Application Tests Complete!")


def test_database_models():
    """Test database models directly"""
    print("\n🗄️ Testing Database Models")
    print("=" * 30)

    try:
        from models import db, Member, MembershipPlan, Trainer, WorkoutSession
        from app import app

        with app.app_context():
            # Test model counts
            member_count = Member.query.count()
            plan_count = MembershipPlan.query.count()
            trainer_count = Trainer.query.count()
            session_count = WorkoutSession.query.count()

            print(f"✅ Members in database: {member_count}")
            print(f"✅ Plans in database: {plan_count}")
            print(f"✅ Trainers in database: {trainer_count}")
            print(f"✅ Sessions in database: {session_count}")

            if member_count > 0 and plan_count > 0 and trainer_count > 0 and session_count > 0:
                print("✅ Database has sample data")
            else:
                print("❌ Database missing sample data")

    except Exception as e:
        print(f"❌ Database model error: {e}")

    print("\n🎯 Database Model Tests Complete!")


if __name__ == "__main__":
    print("🚀 Starting Fitness Club Application Tests")
    print("🔗 Make sure Flask app is running at http://localhost:5000\n")

    test_application()
    test_database_models()

    print("\n" + "=" * 60)
    print("🎉 All Tests Complete!")
    print("✨ If all tests passed, your application is ready for live coding!")
