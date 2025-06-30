"""
Test Runner for Fitness Club Membership System
Run this script to execute all tests and validate the application.
"""
import sys
import os
import subprocess
from datetime import datetime, date

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def run_tests():
    """Run all test suites"""
    print("🎯 Fitness Club Membership System - Test Suite")
    print("=" * 50)
    print(f"Running tests at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Test 1: Import all modules
    print("📦 Testing imports...")
    try:
        from app import app
        from models import db, Member, MembershipPlan, Trainer, WorkoutSession
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

    # Test 2: Database models
    print("\n🗄️ Testing database models...")
    try:
        with app.app_context():
            # Test model creation
            member = Member(
                first_name="Test",
                last_name="User",
                email="test@test.com",
                phone="555-0000",
                date_of_birth="1990-01-01",
                gender="Other",
                emergency_contact="Test Contact",
                emergency_phone="555-0001",
                status="active"
            )
            print("✅ Member model creation successful")

            plan = MembershipPlan(
                name="Test Plan",
                description="Test plan description",
                monthly_price=29.99,
                benefits="Test benefits"
            )
            print("✅ MembershipPlan model creation successful")

            trainer = Trainer(
                name="Test Trainer",
                specialization="Test",
                email="trainer@test.com",
                phone="555-0002"
            )
            print("✅ Trainer model creation successful")

    except Exception as e:
        print(f"❌ Model creation error: {e}")
        return False

    # Test 3: Flask app
    print("\n🌐 Testing Flask application...")
    try:
        with app.test_client() as client:
            # Test homepage
            response = client.get('/')
            if response.status_code == 200:
                print("✅ Homepage accessible")
            else:
                print(f"❌ Homepage error: {response.status_code}")
                return False

            # Test members page
            response = client.get('/members')
            if response.status_code == 200:
                print("✅ Members page accessible")
            else:
                print(f"❌ Members page error: {response.status_code}")
                return False

            # Test plans page
            response = client.get('/plans')
            if response.status_code == 200:
                print("✅ Plans page accessible")
            else:
                print(f"❌ Plans page error: {response.status_code}")
                return False

            # Test sessions page
            response = client.get('/sessions')
            if response.status_code == 200:
                print("✅ Sessions page accessible")
            else:
                print(f"❌ Sessions page error: {response.status_code}")
                return False

    except Exception as e:
        print(f"❌ Flask app error: {e}")
        return False

    # Test 4: Database operations
    print("\n💾 Testing database operations...")
    try:
        with app.app_context():
            # Initialize database
            db.create_all()
            print("✅ Database creation successful")

            # Test data insertion with unique email
            import uuid
            unique_email = f"test_{uuid.uuid4().hex[:8]}@example.com"

            test_member = Member(
                first_name="Test",
                last_name="Member",
                email=unique_email,
                phone="555-1234",
                date_of_birth=date(1990, 1, 1),  # Proper date object
                gender="Other",
                emergency_contact="Emergency",
                emergency_phone="555-5678",
                status="active"
            )

            db.session.add(test_member)
            db.session.commit()
            print("✅ Database insertion successful")

            # Test data retrieval
            retrieved_member = Member.query.filter_by(
                email=unique_email).first()
            if retrieved_member and retrieved_member.first_name == "Test":
                print("✅ Database retrieval successful")
            else:
                print("❌ Database retrieval failed")
                return False

    except Exception as e:
        print(f"❌ Database operations error: {e}")
        return False

    print("\n" + "=" * 50)
    print("🎉 ALL TESTS PASSED! Application is working correctly.")
    print("✅ Ready for live coding demonstration!")
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
