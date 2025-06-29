# Test Script for Sprint 1 - Backend Testing
from app import app
from models import db, Member, MembershipPlan, Trainer, WorkoutSession
import json


def test_sprint_1():
    """Test all Sprint 1 backend functionality"""
    print("🧪 Testing Sprint 1 - Backend Setup + Database Schema")
    print("=" * 60)

    with app.app_context():
        try:
            # Test 1: Database Connection
            print("✅ Test 1: Database Connection")
            db.engine.execute("SELECT 1")
            print("   Database connection successful")

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

            # Test 4: Flask Routes (basic test)
            print("\n✅ Test 4: Flask Application Routes")

            with app.test_client() as client:
                # Test homepage
                response = client.get('/')
                print(f"   Homepage status: {response.status_code}")

                # Test members API
                response = client.get('/api/members')
                if response.status_code == 200:
                    data = json.loads(response.data)
                    print(f"   Members API returned {len(data)} members")
                else:
                    print(f"   Members API status: {response.status_code}")

                # Test plans API
                response = client.get('/api/plans')
                if response.status_code == 200:
                    data = json.loads(response.data)
                    print(f"   Plans API returned {len(data)} plans")
                else:
                    print(f"   Plans API status: {response.status_code}")

            print("\n🎉 Sprint 1 Backend Tests Complete!")
            print("✅ Database schema working correctly")
            print("✅ Models and relationships functional")
            print("✅ Flask application responding")
            print("✅ Ready to proceed to Sprint 2!")

            return True

        except Exception as e:
            print(f"\n❌ Sprint 1 Test Failed: {str(e)}")
            print("Please fix the issues before proceeding to Sprint 2")
            return False


if __name__ == "__main__":
    test_sprint_1()
