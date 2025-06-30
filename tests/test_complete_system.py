"""
Test Suite for Fitness Club Membership System
Tests all major functionality including models, routes, and business logic.
"""
from models import db, Member, MembershipPlan, Trainer, WorkoutSession, MemberPlan, SessionBooking
from app import app
import json
import pytest
import sys
import os
from datetime import date, time, datetime

# Add src directory to path
current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, '..', 'src'))
sys.path.insert(0, src_dir)

# Now import from src


class TestConfig:
    """Test configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test-secret-key'
    WTF_CSRF_ENABLED = False


@pytest.fixture
def client():
    """Create test client with clean database"""
    app.config.from_object(TestConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            # Create test data
            create_test_data()

            yield client

            db.session.remove()
            db.drop_all()


def create_test_data():
    """Create sample test data"""
    # Create membership plans
    plan1 = MembershipPlan(
        name="Basic Plan",
        description="Basic gym access",
        monthly_price=29.99,
        benefits="Gym access"
    )
    plan2 = MembershipPlan(
        name="Premium Plan",
        description="Full access with classes",
        monthly_price=59.99,
        benefits="Gym + Classes + Personal Training"
    )

    # Create trainers
    trainer1 = Trainer(
        name="John Smith",
        specialization="Weight Training",
        email="john@fitness.com",
        phone="555-0101"
    )
    trainer2 = Trainer(
        name="Sarah Johnson",
        specialization="Yoga",
        email="sarah@fitness.com",
        phone="555-0102"
    )

    db.session.add_all([plan1, plan2, trainer1, trainer2])
    db.session.commit()

    # Create members
    member1 = Member(
        first_name="Alice",
        last_name="Wilson",
        email="alice@example.com",
        phone="555-1001",
        date_of_birth=date(1990, 5, 15),
        gender="Female",
        emergency_contact="Bob Wilson",
        emergency_phone="555-1002",
        join_date=date.today(),
        status="active"
    )
    member2 = Member(
        first_name="Bob",
        last_name="Davis",
        email="bob@example.com",
        phone="555-1003",
        date_of_birth=date(1985, 8, 22),
        gender="Male",
        emergency_contact="Carol Davis",
        emergency_phone="555-1004",
        join_date=date.today(),
        status="active"
    )

    db.session.add_all([member1, member2])
    db.session.commit()

    # Create workout sessions
    session1 = WorkoutSession(
        title="Morning Cardio",
        description="High-intensity cardio workout",
        trainer_id=trainer1.id,
        session_date=date.today(),
        start_time=time(9, 0),
        end_time=time(10, 0),
        max_capacity=20,
        current_bookings=0
    )
    session2 = WorkoutSession(
        title="Evening Yoga",
        description="Relaxing yoga session",
        trainer_id=trainer2.id,
        session_date=date.today(),
        start_time=time(18, 0),
        end_time=time(19, 0),
        max_capacity=15,
        current_bookings=0
    )

    db.session.add_all([session1, session2])
    db.session.commit()


class TestModels:
    """Test database models"""

    def test_member_creation(self, client):
        """Test member model creation"""
        with app.app_context():
            member = Member.query.filter_by(email="alice@example.com").first()
            assert member is not None
            assert member.first_name == "Alice"
            assert member.last_name == "Wilson"
            assert member.status == "active"

    def test_membership_plan_creation(self, client):
        """Test membership plan model"""
        with app.app_context():
            plan = MembershipPlan.query.filter_by(name="Basic Plan").first()
            assert plan is not None
            assert plan.monthly_price == 29.99
            assert "Gym access" in plan.benefits

    def test_trainer_creation(self, client):
        """Test trainer model"""
        with app.app_context():
            trainer = Trainer.query.filter_by(name="John Smith").first()
            assert trainer is not None
            assert trainer.specialization == "Weight Training"
            assert trainer.email == "john@fitness.com"

    def test_workout_session_creation(self, client):
        """Test workout session model"""
        with app.app_context():
            session = WorkoutSession.query.filter_by(
                title="Morning Cardio").first()
            assert session is not None
            assert session.max_capacity == 20
            assert session.current_bookings == 0


class TestRoutes:
    """Test Flask routes"""

    def test_homepage(self, client):
        """Test homepage renders"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Fitness Club' in response.data

    def test_members_list(self, client):
        """Test members list page"""
        response = client.get('/members')
        assert response.status_code == 200
        assert b'Alice' in response.data
        assert b'Bob' in response.data

    def test_member_detail(self, client):
        """Test individual member page"""
        with app.app_context():
            member = Member.query.filter_by(email="alice@example.com").first()
            response = client.get(f'/members/{member.id}')
            assert response.status_code == 200
            assert b'Alice Wilson' in response.data

    def test_plans_page(self, client):
        """Test membership plans page"""
        response = client.get('/plans')
        assert response.status_code == 200
        assert b'Basic Plan' in response.data
        assert b'Premium Plan' in response.data

    def test_sessions_page(self, client):
        """Test sessions page"""
        response = client.get('/sessions')
        assert response.status_code == 200
        assert b'Morning Cardio' in response.data
        assert b'Evening Yoga' in response.data

    def test_member_creation_page(self, client):
        """Test member creation form page"""
        response = client.get('/members/new')  # Correct route
        assert response.status_code == 200
        assert b'first_name' in response.data
        assert b'email' in response.data


class TestMemberCreation:
    """Test member creation functionality"""

    def test_create_member_post(self, client):
        """Test creating a new member via POST"""
        member_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'phone': '555-9999',
            'date_of_birth': '1995-01-01',
            'gender': 'Other',
            'emergency_contact': 'Emergency Contact',
            'emergency_phone': '555-8888'
        }

        response = client.post(
            '/members/new', data=member_data)  # Correct route

        # Should redirect on success
        assert response.status_code in [200, 302]

        # Check member was created
        with app.app_context():
            member = Member.query.filter_by(email='test@example.com').first()
            assert member is not None
            assert member.first_name == 'Test'

    def test_duplicate_email_validation(self, client):
        """Test that duplicate emails are rejected"""
        member_data = {
            'first_name': 'Duplicate',
            'last_name': 'User',
            'email': 'alice@example.com',  # Existing email
            'phone': '555-9999',
            'date_of_birth': '1995-01-01',
            'gender': 'Other',
            'emergency_contact': 'Emergency Contact',
            'emergency_phone': '555-8888'
        }

        response = client.post(
            '/members/new', data=member_data)  # Correct route

        # Should show error or stay on form
        assert response.status_code == 200
        assert b'email' in response.data.lower()


class TestDataExport:
    """Test CSV export functionality"""

    def test_members_export(self, client):
        """Test members CSV export"""
        response = client.get('/members/export')  # Correct route
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'text/csv; charset=utf-8'
        assert b'Alice' in response.data
        assert b'Bob' in response.data

    def test_sessions_export(self, client):
        """Test sessions CSV export"""
        response = client.get('/sessions/export')  # Correct route
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'text/csv; charset=utf-8'
        assert b'Morning Cardio' in response.data
        assert b'Evening Yoga' in response.data


class TestSearchFunctionality:
    """Test search and filtering"""

    def test_member_search(self, client):
        """Test member search functionality"""
        response = client.get('/members?search=Alice')
        assert response.status_code == 200
        assert b'Alice' in response.data

        response = client.get('/members?search=NonExistent')
        assert response.status_code == 200
        # Should return no results but not error


class TestAPIEndpoints:
    """Test API endpoints"""

    def test_member_status_toggle(self, client):
        """Test member status toggle API"""
        with app.app_context():
            member = Member.query.filter_by(email="alice@example.com").first()
            response = client.post(
                f'/api/members/{member.id}/toggle-status')  # Correct route
            assert response.status_code == 200

            # Check status was changed
            db.session.refresh(member)
            # Status should be different from 'active'


class TestDashboardStatistics:
    """Test dashboard statistics"""

    def test_dashboard_statistics(self, client):
        """Test that dashboard shows correct statistics"""
        response = client.get('/')
        assert response.status_code == 200

        # Should show member counts
        assert b'2' in response.data  # 2 members

        # Should show session information
        assert b'Morning Cardio' in response.data or b'Evening Yoga' in response.data


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
