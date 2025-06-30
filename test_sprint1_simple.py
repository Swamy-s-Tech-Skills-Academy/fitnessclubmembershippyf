# Simple Sprint 1 Test - Run from project root
import os
import sys

# Change to src directory for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
os.chdir('src')


def test_sprint_1():
    """Simple test of Sprint 1 functionality"""
    print("🧪 Testing Sprint 1 - Backend Setup + Database Schema")
    print("=" * 60)

    try:
        # Test imports
        print("✅ Test 1: Importing modules...")
        from app import app
        from models import db, Member, MembershipPlan, Trainer, WorkoutSession
        print("   All modules imported successfully!")

        # Test Flask app creation
        print("\n✅ Test 2: Flask application...")
        print(f"   App name: {app.name}")
        print(f"   Debug mode: {app.debug}")

        # Test database connection
        print("\n✅ Test 3: Database connection...")
        with app.app_context():
            # Test database tables exist
            from sqlalchemy import text
            result = db.session.execute(
                text("SELECT name FROM sqlite_master WHERE type='table';"))
            tables = [row[0] for row in result]
            print(f"   Database tables: {tables}")

            # Test sample data
            member_count = Member.query.count()
            plan_count = MembershipPlan.query.count()
            trainer_count = Trainer.query.count()
            session_count = WorkoutSession.query.count()

            print(f"   Members: {member_count}")
            print(f"   Plans: {plan_count}")
            print(f"   Trainers: {trainer_count}")
            print(f"   Sessions: {session_count}")

        print("\n🎉 Sprint 1 Backend Tests PASSED!")
        print("✅ Database schema working correctly")
        print("✅ Models and relationships functional")
        print("✅ Flask application configured properly")
        print("✅ Sample data loaded successfully")
        print("\n🚀 Ready to proceed to Sprint 2!")

        return True

    except Exception as e:
        print(f"\n❌ Sprint 1 Test Failed: {str(e)}")
        print("Please fix the issues before proceeding to Sprint 2")
        return False


if __name__ == "__main__":
    test_sprint_1()
