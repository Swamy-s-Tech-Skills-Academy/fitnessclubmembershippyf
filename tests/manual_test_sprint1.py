# Manual Sprint 1 Testing Script
# Simple test runner without external dependencies

from app import app
from models import db, Member, MembershipPlan, MemberPlan, Trainer, WorkoutSession
import sys
import os
from datetime import date, time

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_database_connection():
    """Test database connection and table creation"""
    print("🧪 Testing Database Connection...")

    with app.app_context():
        try:
            # Create tables
            db.create_all()
            print("✅ Database tables created successfully")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False


def test_model_creation():
    """Test creating model instances"""
    print("\n🧪 Testing Model Creation...")

    with app.app_context():
        try:
            # Test Member creation
            member = Member(
                first_name="Test",
                last_name="User",
                email="test@sprint1.com",
                phone="555-TEST",
                date_of_birth=date(1990, 1, 1),
                gender="Male",
                emergency_contact="Emergency Test",
                emergency_phone="555-EMERGENCY"
            )
            db.session.add(member)

            # Test MembershipPlan creation
            plan = MembershipPlan(
                name="Test Plan",
                description="Test membership plan",
                monthly_price=39.99,
                benefits="Test benefits"
            )
            db.session.add(plan)

            # Test Trainer creation
            trainer = Trainer(
                name="Test Trainer",
                specialization="Test Specialty",
                email="trainer@sprint1.com",
                phone="555-TRAINER"
            )
            db.session.add(trainer)

            db.session.commit()
            print("✅ All models created successfully")

            # Verify data
            saved_member = Member.query.filter_by(
                email="test@sprint1.com").first()
            saved_plan = MembershipPlan.query.filter_by(
                name="Test Plan").first()
            saved_trainer = Trainer.query.filter_by(
                name="Test Trainer").first()

            assert saved_member is not None, "Member not saved"
            assert saved_plan is not None, "Plan not saved"
            assert saved_trainer is not None, "Trainer not saved"

            print(
                f"✅ Member ID: {saved_member.id}, Name: {saved_member.first_name} {saved_member.last_name}")
            print(
                f"✅ Plan ID: {saved_plan.id}, Name: {saved_plan.name}, Price: ${saved_plan.monthly_price}")
            print(
                f"✅ Trainer ID: {saved_trainer.id}, Name: {saved_trainer.name}")

            return True

        except Exception as e:
            print(f"❌ Model creation failed: {e}")
            return False


def test_relationships():
    """Test model relationships"""
    print("\n🧪 Testing Model Relationships...")

    with app.app_context():
        try:
            # Get existing data
            member = Member.query.filter_by(email="test@sprint1.com").first()
            plan = MembershipPlan.query.filter_by(name="Test Plan").first()
            trainer = Trainer.query.filter_by(name="Test Trainer").first()

            # Test Member-Plan relationship
            member_plan = MemberPlan(
                member_id=member.id,
                plan_id=plan.id
            )
            db.session.add(member_plan)

            # Test WorkoutSession creation
            session = WorkoutSession(
                title="Test Session",
                description="Test workout session",
                trainer_id=trainer.id,
                session_date=date.today(),
                start_time=time(10, 0),
                end_time=time(11, 0),
                max_capacity=10
            )
            db.session.add(session)

            db.session.commit()

            print("✅ Member-Plan relationship created")
            print("✅ Workout session created with trainer relationship")

            return True

        except Exception as e:
            print(f"❌ Relationship testing failed: {e}")
            return False


def test_flask_routes():
    """Test Flask application routes"""
    print("\n🧪 Testing Flask Routes...")

    with app.test_client() as client:
        try:
            # Test homepage
            response = client.get('/')
            assert response.status_code == 200, f"Homepage failed: {response.status_code}"
            print("✅ Homepage route working")

            # Test members route
            response = client.get('/members')
            assert response.status_code == 200, f"Members route failed: {response.status_code}"
            print("✅ Members list route working")

            # Test member creation form
            response = client.get('/members/create')
            assert response.status_code == 200, f"Member create form failed: {response.status_code}"
            print("✅ Member creation form route working")

            # Test plans route
            response = client.get('/plans')
            assert response.status_code == 200, f"Plans route failed: {response.status_code}"
            print("✅ Plans route working")

            # Test sessions route
            response = client.get('/sessions')
            assert response.status_code == 200, f"Sessions route failed: {response.status_code}"
            print("✅ Sessions route working")

            return True

        except Exception as e:
            print(f"❌ Flask route testing failed: {e}")
            return False


def run_sprint1_tests():
    """Run all Sprint 1 tests"""
    print("🚀 SPRINT 1 TESTING - Backend Setup + Database Schema")
    print("=" * 60)

    # Configure app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    tests = [
        test_database_connection,
        test_model_creation,
        test_relationships,
        test_flask_routes
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")

    print("\n" + "=" * 60)
    print(f"🎯 SPRINT 1 TEST RESULTS: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 SPRINT 1 COMPLETE! Ready for Sprint 2")
        return True
    else:
        print("⚠️  Some tests failed. Please fix issues before Sprint 2")
        return False


if __name__ == "__main__":
    success = run_sprint1_tests()
    sys.exit(0 if success else 1)
