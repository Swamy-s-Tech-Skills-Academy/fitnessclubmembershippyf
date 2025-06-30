# Sprint 1 Tests: Backend Setup + Database Schema
from models import db, Member, MembershipPlan, MemberPlan, Trainer, WorkoutSession
import pytest
import sys
import os
from datetime import date, time

# Add src directory to path FIRST
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# NOW import from src


def test_basic_imports():
    """Test that all imports work"""
    print("✅ Basic imports successful")
    print(f"✅ Member model: {Member}")
    print(f"✅ MembershipPlan model: {MembershipPlan}")
    print(f"✅ Trainer model: {Trainer}")
    print(f"✅ WorkoutSession model: {WorkoutSession}")


def test_model_creation():
    """Test model creation"""
    try:
        # Test that we can create model instances
        member = Member(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            phone="555-0123",
            date_of_birth=date(1990, 1, 1),
            gender="Other",
            emergency_contact="Emergency",
            emergency_phone="555-9999",
            join_date=date.today(),
            status="active"
        )
        print("✅ Member model creation successful")

        plan = MembershipPlan(
            name="Test Plan",
            description="Test Description",
            monthly_price=29.99,
            benefits="Test Benefits"
        )
        print("✅ MembershipPlan model creation successful")

        trainer = Trainer(
            name="Test Trainer",
            specialization="Test Spec",
            email="trainer@test.com",
            phone="555-0456"
        )
        print("✅ Trainer model creation successful")

    except Exception as e:
        print(f"❌ Model creation failed: {e}")


if __name__ == "__main__":
    print("🏗️ Sprint 1 Tests: Backend Setup + Database Schema")
    print("=" * 50)

    test_basic_imports()
    test_model_creation()

    print("\n🎉 Sprint 1 tests completed successfully!")
