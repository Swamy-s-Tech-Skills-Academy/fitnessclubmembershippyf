# Debug script to test the dashboard route data
from datetime import date
from models import db, Member, MembershipPlan, WorkoutSession
from app import app


def test_dashboard_data():
    with app.app_context():
        print("=== DASHBOARD ROUTE DEBUG ===")

        # Replicate the exact queries from the dashboard route
        total_members = Member.query.count()
        active_members = Member.query.filter_by(status='active').count()
        total_sessions = WorkoutSession.query.count()
        upcoming_sessions = WorkoutSession.query.filter(
            WorkoutSession.session_date >= date.today()).count()

        # Recent activities
        recent_members = Member.query.order_by(
            Member.created_at.desc()).limit(5).all()
        upcoming_sessions_list = WorkoutSession.query.filter(
            WorkoutSession.session_date >= date.today()
        ).order_by(WorkoutSession.session_date, WorkoutSession.start_time).limit(5).all()

        print(f"total_members: {total_members}")
        print(f"active_members: {active_members}")
        print(f"total_sessions: {total_sessions}")
        print(f"upcoming_sessions: {upcoming_sessions}")
        print(f"recent_members count: {len(recent_members)}")
        print(f"upcoming_sessions_list count: {len(upcoming_sessions_list)}")

        print("\nTemplate context would be:")
        context = {
            'total_members': total_members,
            'active_members': active_members,
            'total_sessions': total_sessions,
            'upcoming_sessions': upcoming_sessions,
            'recent_members': recent_members,
            'upcoming_sessions_list': upcoming_sessions_list
        }

        for key, value in context.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    test_dashboard_data()
