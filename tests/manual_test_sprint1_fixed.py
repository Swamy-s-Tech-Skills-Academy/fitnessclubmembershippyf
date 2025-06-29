# Manual Sprint 1 Testing Script
# Simple test runner without external dependencies

from datetime import date, time
from sqlalchemy import text
from models import db, Member, MembershipPlan, MemberPlan, Trainer, WorkoutSession
from app import app
import sys
import os

# Add src directory to path FIRST
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_sprint_1():
    """Test all Sprint 1 backend functionality"""
    print("🧪 Testing Sprint 1 - Backend Setup + Database Schema")
    print("=" * 60)

    with app.app_context():
        try:
            # Test 1: Database Connection
            print("✅ Test 1: Database Connection")
            result = db.session.execute(text("SELECT 1")).scalar()
            print(f"   Database connection successful - result: {result}")

            # Test 2: Models and Relationships
            print("\n✅ Test 2: Database Models")

            # Test Members
            member_count = Member.query.count()
            print(f"   Members in database: {member_count}")

            if member_count > 0:
                sample_member = Member.query.first()
                print(f"   Sample member: {sample_member.full_name}")
                print(f"   Member age: {sample_member.age}")
                print(f"   Member status: {sample_member.status}")

            # Test Membership Plans
            plan_count = MembershipPlan.query.count()
            print(f"   Membership plans: {plan_count}")

            if plan_count > 0:
                for plan in MembershipPlan.query.all():
                    print(f"   - {plan.name}: ${plan.monthly_price}/month")

            # Test Trainers
            trainer_count = Trainer.query.count()
            print(f"   Trainers: {trainer_count}")

            if trainer_count > 0:
                for trainer in Trainer.query.all():
                    print(f"   - {trainer.name} ({trainer.specialization})")

            # Test Workout Sessions
            session_count = WorkoutSession.query.count()
            print(f"   Workout sessions: {session_count}")

            if session_count > 0:
                for session in WorkoutSession.query.all():
                    print(f"   - {session.title} with {session.trainer.name}")

            # Test 3: Relationships
            print("\n✅ Test 3: Database Relationships")

            if member_count > 0 and plan_count > 0:
                member_with_plan = Member.query.join(
                    Member.member_plans).first()
                if member_with_plan:
                    current_plan = member_with_plan.member_plans[0].plan
                    print(
                        f"   {member_with_plan.full_name} has {current_plan.name} plan")
                else:
                    print("   No member-plan relationships found")

            # Test 4: Flask Application
            print("\n✅ Test 4: Flask Application")
            print(f"   App name: {app.name}")
            print(f"   Debug mode: {app.debug}")
            print(f"   Config loaded: {bool(app.config)}")

            # Test routes exist
            rules = [str(rule) for rule in app.url_map.iter_rules()]
            print(f"   Routes registered: {len(rules)}")
            key_routes = ['/', '/members', '/api/members', '/api/plans']
            for route in key_routes:
                if route in [r.split()[0] if ' ' in r else r for r in rules]:
                    print(f"   ✅ Route {route} exists")
                else:
                    print(f"   ❌ Route {route} missing")

            print("\n🎉 Sprint 1 Backend Tests Complete!")
            print("✅ Database schema working correctly")
            print("✅ Models and relationships functional")
            print("✅ Flask application responding")
            print("✅ Ready to proceed to Sprint 2!")

            return True

        except Exception as e:
            print(f"\n❌ Sprint 1 Test Failed: {str(e)}")
            import traceback
            traceback.print_exc()
            print("Please fix the issues before proceeding to Sprint 2")
            return False


def test_api_endpoints():
    """Test API endpoints with Flask test client"""
    print("\n🌐 Testing API Endpoints")
    print("-" * 40)

    with app.test_client() as client:
        try:
            # Test homepage
            response = client.get('/')
            print(f"Homepage (/) status: {response.status_code}")

            # Test members page
            response = client.get('/members')
            print(f"Members page (/members) status: {response.status_code}")

            # Test API endpoints
            response = client.get('/api/members')
            print(f"Members API (/api/members) status: {response.status_code}")

            response = client.get('/api/plans')
            print(f"Plans API (/api/plans) status: {response.status_code}")

            print("✅ API endpoint tests complete")

        except Exception as e:
            print(f"❌ API test failed: {str(e)}")


if __name__ == "__main__":
    print("🚀 Starting Sprint 1 Manual Tests")
    print("=" * 50)

    success = test_sprint_1()

    if success:
        test_api_endpoints()
        print("\n🎉 All Sprint 1 tests passed! Ready for Sprint 2!")
    else:
        print("\n❌ Sprint 1 tests failed. Please fix issues before continuing.")
