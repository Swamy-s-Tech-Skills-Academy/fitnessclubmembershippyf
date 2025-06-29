# Pre-Sprint Validation Script
# Run this from the project root to validate Sprint 1 setup

import os
import sys


def validate_pre_sprint():
    """Validate that Pre-Sprint setup is complete and ready for development"""
    print("🔍 Pre-Sprint Validation")
    print("=" * 50)

    # Check 1: Virtual Environment
    print("\n✅ Check 1: Virtual Environment")
    if 'VIRTUAL_ENV' in os.environ:
        print(f"   Active: {os.environ['VIRTUAL_ENV']}")
    else:
        print("   ⚠️  Warning: Virtual environment not detected")
        print("   Run: .venv\\Scripts\\activate")

    # Check 2: Dependencies
    print("\n✅ Check 2: Dependencies")
    try:
        import flask
        import flask_sqlalchemy
        print(f"   Flask: {flask.__version__}")
        print(f"   SQLAlchemy: {flask_sqlalchemy.__version__}")
    except ImportError as e:
        print(f"   ❌ Missing dependency: {e}")
        print("   Run: pip install -r requirements.txt")

    # Check 3: Project Structure
    print("\n✅ Check 3: Project Structure")
    required_paths = [
        'src/app.py',
        'src/models.py',
        'src/init_db.py',
        'tests/manual_test_sprint1_fixed.py',
        'requirements.txt'
    ]

    for path in required_paths:
        if os.path.exists(path):
            print(f"   ✓ {path}")
        else:
            print(f"   ❌ Missing: {path}")

    # Check 4: Database
    print("\n✅ Check 4: Database")
    db_path = 'src/instance/fitness_club.db'
    if os.path.exists(db_path):
        print(f"   ✓ Database exists: {db_path}")
        size = os.path.getsize(db_path)
        print(f"   Database size: {size} bytes")
    else:
        print(f"   ❌ Database not found: {db_path}")
        print("   Run: cd src && python init_db.py")

    # Check 5: Import Test
    print("\n✅ Check 5: Import Test")
    try:
        # Add src to path temporarily
        sys.path.insert(0, 'src')

        from app import app
        from models import db, Member, MembershipPlan

        print("   ✓ App imports successful")

        # Test app context
        with app.app_context():
            member_count = Member.query.count()
            plan_count = MembershipPlan.query.count()
            print(f"   ✓ Members in DB: {member_count}")
            print(f"   ✓ Plans in DB: {plan_count}")

        sys.path.remove('src')

    except Exception as e:
        print(f"   ❌ Import error: {str(e)}")
        if 'src' in sys.path:
            sys.path.remove('src')

    # Final Assessment
    print("\n🎯 Pre-Sprint Assessment")
    print("=" * 50)

    if all([
        'VIRTUAL_ENV' in os.environ,
        os.path.exists('src/app.py'),
        os.path.exists('src/instance/fitness_club.db')
    ]):
        print("🎉 PRE-SPRINT VALIDATION PASSED!")
        print("✅ Ready to proceed with Sprint development")
        print("\nNext steps:")
        print("1. cd src")
        print("2. python app.py")
        print("3. Open http://localhost:5000")
    else:
        print("⚠️  PRE-SPRINT VALIDATION INCOMPLETE")
        print("❌ Please complete setup steps before proceeding")
        print("\nRefer to: docs/pre-sprint-setup.md")


if __name__ == "__main__":
    validate_pre_sprint()
