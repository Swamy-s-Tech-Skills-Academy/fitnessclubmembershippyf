# Main Flask Application for Fitness Club Membership System
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
import os

from config import Config
from models import db, Member, MembershipPlan, MemberPlan, Trainer, WorkoutSession, SessionBooking


def create_app():
    """Application factory pattern for Flask app creation"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    """Homepage with dashboard overview"""
    # Get dashboard statistics
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

    return render_template('index.html',
                           total_members=total_members,
                           active_members=active_members,
                           total_sessions=total_sessions,
                           upcoming_sessions=upcoming_sessions,
                           recent_members=recent_members,
                           upcoming_sessions_list=upcoming_sessions_list)

# Member Routes


@app.route('/members')
def members():
    """List all members with search functionality"""
    search = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)

    query = Member.query

    if search:
        query = query.filter(
            (Member.first_name.contains(search)) |
            (Member.last_name.contains(search)) |
            (Member.email.contains(search))
        )

    members = query.order_by(Member.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )

    return render_template('members/list.html', members=members, search=search)


@app.route('/members/new', methods=['GET', 'POST'])
def new_member():
    """Create new member"""
    if request.method == 'POST':
        try:
            member = Member(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                phone=request.form.get('phone'),
                date_of_birth=datetime.strptime(
                    request.form['date_of_birth'], '%Y-%m-%d').date() if request.form.get('date_of_birth') else None,
                gender=request.form.get('gender'),
                emergency_contact=request.form.get('emergency_contact'),
                emergency_phone=request.form.get('emergency_phone')
            )

            db.session.add(member)
            db.session.commit()

            # Assign membership plan if selected
            if request.form.get('plan_id'):
                member_plan = MemberPlan(
                    member_id=member.id,
                    plan_id=int(request.form['plan_id'])
                )
                db.session.add(member_plan)
                db.session.commit()

            flash('Member registered successfully!', 'success')
            return redirect(url_for('members'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error registering member: {str(e)}', 'error')

    plans = MembershipPlan.query.all()
    return render_template('members/create.html', plans=plans)


@app.route('/members/<int:id>')
def member_detail(id):
    """View member details"""
    member = Member.query.get_or_404(id)
    return render_template('members/detail.html', member=member)


@app.route('/members/<int:id>/edit', methods=['GET', 'POST'])
def edit_member(id):
    """Edit member information"""
    member = Member.query.get_or_404(id)

    if request.method == 'POST':
        try:
            member.first_name = request.form['first_name']
            member.last_name = request.form['last_name']
            member.email = request.form['email']
            member.phone = request.form.get('phone')
            member.date_of_birth = datetime.strptime(
                request.form['date_of_birth'], '%Y-%m-%d').date() if request.form.get('date_of_birth') else None
            member.gender = request.form.get('gender')
            member.emergency_contact = request.form.get('emergency_contact')
            member.emergency_phone = request.form.get('emergency_phone')
            member.status = request.form.get('status', 'active')

            db.session.commit()
            flash('Member updated successfully!', 'success')
            return redirect(url_for('member_detail', id=id))

        except Exception as e:
            db.session.rollback()
            flash(f'Error updating member: {str(e)}', 'error')

    return render_template('members/edit.html', member=member)

# Plans Routes


@app.route('/plans')
def plans():
    """List all membership plans"""
    plans = MembershipPlan.query.all()
    return render_template('plans/list.html', plans=plans)

# Sessions Routes


@app.route('/sessions')
def sessions():
    """List all workout sessions"""
    page = request.args.get('page', 1, type=int)
    sessions = WorkoutSession.query.filter(
        WorkoutSession.session_date >= date.today()
    ).order_by(WorkoutSession.session_date, WorkoutSession.start_time).paginate(
        page=page, per_page=10, error_out=False
    )

    return render_template('sessions/list.html', sessions=sessions)


@app.route('/sessions/new', methods=['GET', 'POST'])
def new_session():
    """Create new workout session"""
    if request.method == 'POST':
        try:
            session = WorkoutSession(
                title=request.form['title'],
                description=request.form.get('description'),
                trainer_id=int(request.form['trainer_id']) if request.form.get(
                    'trainer_id') else None,
                session_date=datetime.strptime(
                    request.form['session_date'], '%Y-%m-%d').date(),
                start_time=datetime.strptime(
                    request.form['start_time'], '%H:%M').time(),
                end_time=datetime.strptime(
                    request.form['end_time'], '%H:%M').time(),
                max_capacity=int(request.form.get('max_capacity', 10))
            )

            db.session.add(session)
            db.session.commit()

            flash('Session scheduled successfully!', 'success')
            return redirect(url_for('sessions'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error scheduling session: {str(e)}', 'error')

    trainers = Trainer.query.all()
    return render_template('sessions/schedule.html', trainers=trainers)


@app.route('/sessions/<int:id>/book', methods=['POST'])
def book_session(id):
    """Book a workout session"""
    session = WorkoutSession.query.get_or_404(id)
    member_id = request.form.get('member_id')

    if not member_id:
        flash('Please select a member', 'error')
        return redirect(url_for('sessions'))

    if session.is_full:
        flash('Session is fully booked', 'error')
        return redirect(url_for('sessions'))

    # Check if member already booked this session
    existing_booking = SessionBooking.query.filter_by(
        member_id=member_id, session_id=id
    ).first()

    if existing_booking:
        flash('Member already booked this session', 'error')
        return redirect(url_for('sessions'))

    try:
        booking = SessionBooking(
            member_id=int(member_id),
            session_id=id
        )

        db.session.add(booking)
        session.current_bookings += 1
        db.session.commit()

        flash('Session booked successfully!', 'success')

    except Exception as e:
        db.session.rollback()
        flash(f'Error booking session: {str(e)}', 'error')

    return redirect(url_for('sessions'))


def init_db():
    """Initialize database with sample data"""
    with app.app_context():
        db.create_all()

        # Create sample membership plans
        if MembershipPlan.query.count() == 0:
            plans = [
                MembershipPlan(
                    name='Basic',
                    description='Access to gym equipment',
                    monthly_price=29.99,
                    benefits='Gym access, Locker room'
                ),
                MembershipPlan(
                    name='Pro',
                    description='Gym + Group classes',
                    monthly_price=49.99,
                    benefits='Gym access, Group classes, Locker room'
                ),
                MembershipPlan(
                    name='Elite',
                    description='Full access + Personal training',
                    monthly_price=79.99,
                    benefits='All Pro benefits + 2 personal training sessions/month'
                )
            ]

            for plan in plans:
                db.session.add(plan)

        # Create sample trainers
        if Trainer.query.count() == 0:
            trainers = [
                Trainer(name='Sarah Johnson', specialization='Yoga & Pilates',
                        email='sarah@fitclub.com', phone='555-0101'),
                Trainer(name='Mike Torres', specialization='Strength Training',
                        email='mike@fitclub.com', phone='555-0102'),
                Trainer(name='Emma Davis', specialization='Cardio & HIIT',
                        email='emma@fitclub.com', phone='555-0103')
            ]

            for trainer in trainers:
                db.session.add(trainer)

        db.session.commit()
        print("Database initialized with sample data!")


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
