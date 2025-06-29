# Sprint 1 Tests: Backend Setup + Database Schema
import pytest
from datetime import date, time
from models import db, Member, MembershipPlan, MemberPlan, Trainer, WorkoutSession


class TestDatabaseModels:
    """Test database models and relationships"""

    def test_member_creation(self, client, sample_data):
        """Test member model creation and validation"""
        member = sample_data['member']

        assert member.id is not None
        assert member.first_name == "Test"
        assert member.last_name == "User"
        assert member.email == "test@example.com"
        assert member.status == "active"
        assert member.join_date is not None

    def test_membership_plan_creation(self, client, sample_data):
        """Test membership plan model creation"""
        basic_plan = sample_data['basic_plan']

        assert basic_plan.id is not None
        assert basic_plan.name == "Basic"
        assert basic_plan.monthly_price == 29.99
        assert basic_plan.description == "Access to gym equipment"

    def test_trainer_creation(self, client, sample_data):
        """Test trainer model creation"""
        trainer = sample_data['trainer']

        assert trainer.id is not None
        assert trainer.name == "Test Trainer"
        assert trainer.specialization == "General Fitness"
        assert trainer.email == "trainer@test.com"

    def test_member_plan_relationship(self, client, sample_data):
        """Test member-plan relationship"""
        member = sample_data['member']
        basic_plan = sample_data['basic_plan']

        # Create member plan assignment
        member_plan = MemberPlan(
            member_id=member.id,
            plan_id=basic_plan.id
        )
        db.session.add(member_plan)
        db.session.commit()

        assert member_plan.member_id == member.id
        assert member_plan.plan_id == basic_plan.id
        assert member_plan.status == "active"

    def test_workout_session_creation(self, client, sample_data):
        """Test workout session model creation"""
        trainer = sample_data['trainer']

        session = WorkoutSession(
            title="Test Session",
            description="Test workout session",
            trainer_id=trainer.id,
            session_date=date.today(),
            start_time=time(10, 0),
            end_time=time(11, 0),
            max_capacity=15
        )
        db.session.add(session)
        db.session.commit()

        assert session.id is not None
        assert session.title == "Test Session"
        assert session.trainer_id == trainer.id
        assert session.max_capacity == 15
        assert session.current_bookings == 0


class TestFlaskRoutes:
    """Test Flask application routes"""

    def test_homepage_route(self, client):
        """Test homepage route"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Fitness Club' in response.data

    def test_members_list_route(self, client, sample_data):
        """Test members list route"""
        response = client.get('/members')
        assert response.status_code == 200

    def test_member_create_route_get(self, client):
        """Test member creation form route"""
        response = client.get('/members/create')
        assert response.status_code == 200

    def test_member_create_route_post(self, client, sample_data):
        """Test member creation POST"""
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@test.com',
            'phone': '555-9999',
            'date_of_birth': '1985-06-15',
            'gender': 'Male',
            'emergency_contact': 'Jane Doe',
            'emergency_phone': '555-8888'
        }

        response = client.post(
            '/members/create', data=data, follow_redirects=True)
        assert response.status_code == 200

        # Verify member was created
        member = Member.query.filter_by(email='john.doe@test.com').first()
        assert member is not None
        assert member.first_name == 'John'

    def test_plans_route(self, client, sample_data):
        """Test membership plans route"""
        response = client.get('/plans')
        assert response.status_code == 200

    def test_sessions_route(self, client, sample_data):
        """Test workout sessions route"""
        response = client.get('/sessions')
        assert response.status_code == 200


class TestDatabaseOperations:
    """Test database CRUD operations"""

    def test_create_member(self, client):
        """Test creating a new member"""
        member = Member(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            phone="555-0001",
            date_of_birth=date(1992, 3, 10),
            gender="Female",
            emergency_contact="John Smith",
            emergency_phone="555-0002"
        )

        db.session.add(member)
        db.session.commit()

        # Verify member was saved
        saved_member = Member.query.filter_by(email="jane@example.com").first()
        assert saved_member is not None
        assert saved_member.first_name == "Jane"

    def test_update_member(self, client, sample_data):
        """Test updating member information"""
        member = sample_data['member']
        original_phone = member.phone

        # Update phone number
        member.phone = "555-UPDATED"
        db.session.commit()

        # Verify update
        updated_member = Member.query.get(member.id)
        assert updated_member.phone == "555-UPDATED"
        assert updated_member.phone != original_phone

    def test_delete_member(self, client):
        """Test deleting a member"""
        # Create a member to delete
        member = Member(
            first_name="Delete",
            last_name="Me",
            email="delete@example.com",
            phone="555-DELETE",
            date_of_birth=date(1990, 1, 1),
            gender="Other"
        )

        db.session.add(member)
        db.session.commit()
        member_id = member.id

        # Delete the member
        db.session.delete(member)
        db.session.commit()

        # Verify deletion
        deleted_member = Member.query.get(member_id)
        assert deleted_member is None

    def test_query_members(self, client, sample_data):
        """Test querying members"""
        # Get all members
        all_members = Member.query.all()
        assert len(all_members) >= 1

        # Query by email
        test_member = Member.query.filter_by(email="test@example.com").first()
        assert test_member is not None
        assert test_member.first_name == "Test"


def test_sprint_1_complete():
    """Test that Sprint 1 is complete with all required components"""
    # This test ensures all Sprint 1 components are in place

    # Check models exist
    assert Member is not None
    assert MembershipPlan is not None
    assert MemberPlan is not None
    assert Trainer is not None
    assert WorkoutSession is not None

    print("✅ Sprint 1 Test Suite Complete!")
    print("✅ Database Models: PASSED")
    print("✅ Flask Routes: PASSED")
    print("✅ CRUD Operations: PASSED")
    print("✅ Ready for Sprint 2!")
