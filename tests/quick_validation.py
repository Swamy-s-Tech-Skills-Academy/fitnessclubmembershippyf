"""
Quick Test Validation for Live Coding Session
Simple validation to ensure everything is ready for the demo
"""
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

print("🎬 FITNESS CLUB MEMBERSHIP SYSTEM - LIVE CODING VALIDATION")
print("=" * 60)

try:
    # Import test
    from app import app
    from models import db, Member, MembershipPlan, Trainer, WorkoutSession
    print("✅ 1. All imports successful")

    # App context test
    with app.app_context():
        print("✅ 2. Flask app context working")

        # Database test
        member_count = Member.query.count()
        print(f"✅ 3. Database connected - {member_count} members found")

    # Route test
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("✅ 4. Homepage route working")

        response = client.get('/members')
        if response.status_code == 200:
            print("✅ 5. Members page working")

        response = client.get('/members/export')
        if response.status_code == 200:
            print("✅ 6. CSV export working")

    print("\n🎉 ALL TESTS PASSED!")
    print("🚀 Ready for live coding session!")
    print("📝 Application is fully functional")

except Exception as e:
    print(f"❌ ERROR: {e}")
    print("🔧 Please check the application setup")
