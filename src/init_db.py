# Database Initialization Script for Fitness Club Membership System
from app import app
from models import db, Member, MembershipPlan, MemberPlan, Trainer, WorkoutSession
from datetime import datetime, date, time


def init_database():
    """Initialize database with tables and sample data"""
    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()

        # Check if data already exists
        if MembershipPlan.query.first():
            print("Database already initialized with sample data.")
            return

        # Create sample membership plans
        print("Creating sample membership plans...")
        plans = [
            MembershipPlan(
                name="Basic",
                description="Access to gym equipment",
                monthly_price=29.99,
                benefits="Gym access, Locker room"
            ),
            MembershipPlan(
                name="Pro",
                description="Gym + Group classes",
                monthly_price=49.99,
                benefits="Gym access, Group classes, Locker room"
            ),
            MembershipPlan(
                name="Elite",
                description="Full access + Personal training",
                monthly_price=79.99,
                benefits="All Pro benefits + 2 personal training sessions/month"
            )
        ]

        for plan in plans:
            db.session.add(plan)

        # Create sample trainers
        print("Creating sample trainers...")
        trainers = [
            Trainer(
                name="Sarah Johnson",
                specialization="Yoga & Pilates",
                email="sarah@fitclub.com",
                phone="555-0101"
            ),
            Trainer(
                name="Mike Torres",
                specialization="Strength Training",
                email="mike@fitclub.com",
                phone="555-0102"
            ),
            Trainer(
                name="Emma Davis",
                specialization="Cardio & HIIT",
                email="emma@fitclub.com",
                phone="555-0103"
            )
        ]

        for trainer in trainers:
            db.session.add(trainer)

        # Create sample members
        print("Creating sample members...")
        members = [
            Member(
                first_name="John",
                last_name="Doe",
                email="john.doe@example.com",
                phone="555-1001",
                date_of_birth=date(1990, 5, 15),
                gender="Male",
                emergency_contact="Jane Doe",
                emergency_phone="555-1002"
            ),
            Member(
                first_name="Alice",
                last_name="Smith",
                email="alice.smith@example.com",
                phone="555-2001",
                date_of_birth=date(1985, 8, 22),
                gender="Female",
                emergency_contact="Bob Smith",
                emergency_phone="555-2002"
            ),
            Member(
                first_name="Bob",
                last_name="Wilson",
                email="bob.wilson@example.com",
                phone="555-3001",
                date_of_birth=date(1992, 12, 3),
                gender="Male",
                emergency_contact="Mary Wilson",
                emergency_phone="555-3002"
            )
        ]

        for member in members:
            db.session.add(member)

        # Commit all data
        db.session.commit()

        # Assign membership plans to members
        print("Assigning membership plans...")
        john = Member.query.filter_by(email="john.doe@example.com").first()
        alice = Member.query.filter_by(email="alice.smith@example.com").first()
        bob = Member.query.filter_by(email="bob.wilson@example.com").first()

        basic_plan = MembershipPlan.query.filter_by(name="Basic").first()
        pro_plan = MembershipPlan.query.filter_by(name="Pro").first()
        elite_plan = MembershipPlan.query.filter_by(name="Elite").first()

        member_plans = [
            MemberPlan(member_id=john.id, plan_id=pro_plan.id),
            MemberPlan(member_id=alice.id, plan_id=elite_plan.id),
            MemberPlan(member_id=bob.id, plan_id=basic_plan.id)
        ]

        for mp in member_plans:
            db.session.add(mp)

        # Create sample workout sessions
        print("Creating sample workout sessions...")
        sarah = Trainer.query.filter_by(name="Sarah Johnson").first()
        mike = Trainer.query.filter_by(name="Mike Torres").first()
        emma = Trainer.query.filter_by(name="Emma Davis").first()

        sessions = [
            WorkoutSession(
                title="Morning Yoga",
                description="Relaxing yoga session to start your day",
                trainer_id=sarah.id,
                session_date=date.today(),
                start_time=time(7, 0),
                end_time=time(8, 0),
                max_capacity=15
            ),
            WorkoutSession(
                title="Strength Training",
                description="Build muscle with guided strength exercises",
                trainer_id=mike.id,
                session_date=date.today(),
                start_time=time(18, 0),
                end_time=time(19, 0),
                max_capacity=10
            ),
            WorkoutSession(
                title="HIIT Cardio",
                description="High intensity interval training for maximum burn",
                trainer_id=emma.id,
                session_date=date.today(),
                start_time=time(19, 30),
                end_time=time(20, 30),
                max_capacity=12
            )
        ]

        for session in sessions:
            db.session.add(session)

        db.session.commit()

        print("✅ Database initialized successfully!")
        print(f"Created {len(plans)} membership plans")
        print(f"Created {len(trainers)} trainers")
        print(f"Created {len(members)} members")
        print(f"Created {len(sessions)} workout sessions")


if __name__ == "__main__":
    init_database()
