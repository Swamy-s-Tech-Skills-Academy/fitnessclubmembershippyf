# Quick database test script
from datetime import date
from models import db, Member, MembershipPlan, WorkoutSession
from app import app
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_database():
    with app.app_context():
        print("=== DATABASE TEST ===")

        # Test Member count
        total_members = Member.query.count()
        print(f"Total Members in DB: {total_members}")

        if total_members > 0:
            members = Member.query.all()
            for member in members:
                print(
                    f"  - {member.first_name} {member.last_name} (Status: {member.status})")

        # Test active members
        active_members = Member.query.filter_by(status='active').count()
        print(f"Active Members: {active_members}")

        # Test plans
        total_plans = MembershipPlan.query.count()
        print(f"Total Plans: {total_plans}")

        if total_plans > 0:
            plans = MembershipPlan.query.all()
            for plan in plans:
                print(f"  - {plan.name}: ${plan.monthly_price}")

        # Test sessions
        total_sessions = WorkoutSession.query.count()
        print(f"Total Sessions: {total_sessions}")

        upcoming_sessions = WorkoutSession.query.filter(
            WorkoutSession.session_date >= date.today()).count()
        print(f"Upcoming Sessions: {upcoming_sessions}")

        if total_sessions > 0:
            sessions = WorkoutSession.query.all()
            for session in sessions:
                print(f"  - {session.title} on {session.session_date}")


if __name__ == "__main__":
    test_database()
