# Test Configuration for Fitness Club Membership System
from models import db, Member, MembershipPlan, Trainer, WorkoutSession
from app import app
import os
import sys
import tempfile
import pytest
from datetime import date, time

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Now import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestConfig:
    """Configuration for testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for tests
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test-secret-key'
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config.from_object(TestConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


@pytest.fixture
def sample_data():
    """Create sample data for testing"""
    # Create membership plans
    basic_plan = MembershipPlan(
        name="Basic",
        description="Access to gym equipment",
        monthly_price=29.99,
        benefits="Gym access, Locker room"
    )

    pro_plan = MembershipPlan(
        name="Pro",
        description="Gym + Group classes",
        monthly_price=49.99,
        benefits="Gym access, Group classes, Locker room"
    )

    db.session.add(basic_plan)
    db.session.add(pro_plan)

    # Create a trainer
    trainer = Trainer(
        name="Test Trainer",
        specialization="General Fitness",
        email="trainer@test.com",
        phone="555-0000"
    )
    db.session.add(trainer)

    # Create a member
    member = Member(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        phone="555-1234",
        date_of_birth=date(1990, 1, 1),
        gender="Male",
        emergency_contact="Emergency Contact",
        emergency_phone="555-5678"
    )
    db.session.add(member)

    db.session.commit()

    return {
        'basic_plan': basic_plan,
        'pro_plan': pro_plan,
        'trainer': trainer,
        'member': member
    }
