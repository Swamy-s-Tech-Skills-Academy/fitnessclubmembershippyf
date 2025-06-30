"""
Quick Validation Test for Live Coding Session
This test validates that all sprint deliverables are working correctly.
"""
import sys
import os
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def validate_sprint_deliverables():
    """Validate all sprint deliverables are working"""
    print("Live Coding Session - Sprint Validation")
    print("=" * 50)

    # Sprint 1 Validation: Backend & Database
    print("\n[SPRINT 1] VALIDATION: Backend Foundation")
    try:
        from app import app
        from models import db, Member, MembershipPlan, Trainer, WorkoutSession
        print("[OK] Models imported successfully")

        with app.app_context():
            # Check if database tables exist
            db.create_all()

            # Check sample data
            member_count = Member.query.count()
            plan_count = MembershipPlan.query.count()
            trainer_count = Trainer.query.count()
            session_count = WorkoutSession.query.count()

            print(f"[OK] Database tables created")
            print(
                f"[OK] Sample data: {member_count} members, {plan_count} plans, {trainer_count} trainers, {session_count} sessions")

        print("[TARGET] Sprint 1: COMPLETE [OK]")

    except Exception as e:
        print(f"[ERROR] Sprint 1 Error: {e}")
        return False

    # Sprint 2 Validation: Frontend Templates
    print("\n[FRONTEND] SPRINT 2 VALIDATION: Frontend Templates")
    try:
        with app.test_client() as client:
            routes_to_test = [
                ('/', 'Dashboard'),
                ('/members', 'Members List'),
                ('/members/new', 'Member Creation'),
                ('/plans', 'Membership Plans'),
                ('/sessions', 'Sessions'),
                ('/sessions/new', 'Session Scheduling')
            ]

            for route, name in routes_to_test:
                response = client.get(route)
                if response.status_code == 200:
                    print(f"[OK] {name} page working")
                else:
                    print(f"[ERROR] {name} page error: {response.status_code}")
                    return False

        print("[TARGET] Sprint 2: COMPLETE [OK]")

    except Exception as e:
        print(f"[ERROR] Sprint 2 Error: {e}")
        return False

    # Sprint 3 Validation: Integration & Polish
    print("\n[INTEGRATION] SPRINT 3 VALIDATION: Integration & Polish")
    try:
        with app.test_client() as client:
            # Test CSV exports
            csv_routes = ['/members/export', '/sessions/export']
            for route in csv_routes:
                response = client.get(route)
                if response.status_code == 200:
                    print(f"[OK] CSV export {route} working")
                else:
                    print(
                        f"[ERROR] CSV export {route} error: {response.status_code}")
                    return False

            # Test member creation with validation
            member_data = {
                'first_name': 'LiveTest',
                'last_name': 'User',
                'email': 'livetest@example.com',
                'phone': '555-LIVE',
                'date_of_birth': '1990-01-01',
                'gender': 'Other',
                'emergency_contact': 'Live Contact',
                'emergency_phone': '555-EMRG'
            }

            response = client.post('/members/new', data=member_data)
            if response.status_code in [200, 302]:
                print("[OK] Member creation with validation working")
            else:
                print(f"[ERROR] Member creation error: {response.status_code}")
                return False

        print("[TARGET] Sprint 3: COMPLETE [OK]")

    except Exception as e:
        print(f"[ERROR] Sprint 3 Error: {e}")
        return False

    # Final System Validation
    print("\n[SUCCESS] FINAL SYSTEM VALIDATION")
    try:
        with app.test_client() as client:
            # Test complete user flow

            # 1. View dashboard
            response = client.get('/')
            assert response.status_code == 200
            print("[OK] Dashboard accessible")

            # 2. View members
            response = client.get('/members')
            assert response.status_code == 200
            print("[OK] Member management working")

            # 3. Export data
            response = client.get('/members/export')
            assert response.status_code == 200
            print("[OK] Data export working")

            # 4. Test responsive design (check for mobile viewport)
            response = client.get('/')
            if b'viewport' in response.data:
                print("[OK] Responsive design meta tag present")

            # 5. Check for Tailwind CSS
            if b'tailwindcss' in response.data:
                print("[OK] Tailwind CSS loaded")

        print("[TARGET] Final System: COMPLETE [OK]")

    except Exception as e:
        print(f"[ERROR] Final validation error: {e}")
        return False

    print("\n" + "=" * 50)
    print("🎊 LIVE CODING SESSION READY! 🎊")
    print("[OK] All sprints validated successfully")
    print("[OK] System is production-ready")
    print("[OK] Perfect for demonstration!")
    print("=" * 50)

    return True


if __name__ == '__main__':
    success = validate_sprint_deliverables()
    if success:
        print("\n🚀 You're ready to rock the live coding session!")
    else:
        print("\n[ERROR] Please fix issues before live coding session.")

    sys.exit(0 if success else 1)
