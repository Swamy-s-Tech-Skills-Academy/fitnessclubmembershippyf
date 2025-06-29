# Main Flask Application for Fitness Club Membership System
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
import os
import csv
import io

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


# Context processor to make request.endpoint available in templates
@app.context_processor
def inject_template_vars():
    from flask import request
    return {
        'current_endpoint': request.endpoint,
        'request': request
    }


@app.route('/')
def index():
    """Homepage with dashboard overview"""
    # Get dashboard statistics
    total_members = Member.query.count()
    active_members = Member.query.filter_by(status='active').count()
    inactive_members = Member.query.filter_by(status='inactive').count()
    total_sessions = WorkoutSession.query.count()
    upcoming_sessions = WorkoutSession.query.filter(
        WorkoutSession.session_date >= date.today()).count()

    # Revenue calculation (estimated monthly)
    total_revenue = 0
    active_memberships = db.session.query(MemberPlan, MembershipPlan).join(
        MembershipPlan, MemberPlan.plan_id == MembershipPlan.id
    ).join(Member, MemberPlan.member_id == Member.id).filter(
        Member.status == 'active'
    ).all()

    for _, plan in active_memberships:
        total_revenue += plan.monthly_price

    # Session statistics
    today_sessions = WorkoutSession.query.filter(
        WorkoutSession.session_date == date.today()).count()

    # Get popular plans
    plan_stats = db.session.query(
        MembershipPlan.name,
        db.func.count(MemberPlan.id).label('member_count')
    ).join(MemberPlan).group_by(MembershipPlan.id).all()

    # Recent activities
    recent_members = Member.query.order_by(
        Member.created_at.desc()).limit(5).all()
    upcoming_sessions_list = WorkoutSession.query.filter(
        WorkoutSession.session_date >= date.today()
    ).order_by(WorkoutSession.session_date, WorkoutSession.start_time).limit(5).all()

    # Calculate growth metrics (simplified - comparing with last month placeholder)
    member_growth = 15.2  # This would be calculated from historical data
    revenue_growth = 8.7  # This would be calculated from historical data

    return render_template('index.html',
                           total_members=total_members,
                           active_members=active_members,
                           inactive_members=inactive_members,
                           total_sessions=total_sessions,
                           upcoming_sessions=upcoming_sessions,
                           today_sessions=today_sessions,
                           total_revenue=total_revenue,
                           member_growth=member_growth,
                           revenue_growth=revenue_growth,
                           plan_stats=plan_stats,
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
        # Validation
        errors = []

        # Required field validation
        if not request.form.get('first_name', '').strip():
            errors.append('First name is required')
        if not request.form.get('last_name', '').strip():
            errors.append('Last name is required')
        if not request.form.get('email', '').strip():
            errors.append('Email is required')

        # Email validation
        email = request.form.get('email', '').strip()
        if email and '@' not in email:
            errors.append('Please enter a valid email address')

        # Check for duplicate email
        if email and Member.query.filter_by(email=email).first():
            errors.append('A member with this email already exists')

        # Date validation
        date_of_birth = None
        if request.form.get('date_of_birth'):
            try:
                date_of_birth = datetime.strptime(
                    request.form['date_of_birth'], '%Y-%m-%d').date()
                if date_of_birth > date.today():
                    errors.append('Date of birth cannot be in the future')
            except ValueError:
                errors.append('Please enter a valid date of birth')

        if errors:
            for error in errors:
                flash(error, 'error')
            plans = MembershipPlan.query.all()
            return render_template('members/create.html', plans=plans)

        try:
            member = Member(
                first_name=request.form['first_name'].strip(),
                last_name=request.form['last_name'].strip(),
                email=email,
                phone=request.form.get('phone', '').strip() or None,
                date_of_birth=date_of_birth,
                gender=request.form.get('gender'),
                emergency_contact=request.form.get(
                    'emergency_contact', '').strip() or None,
                emergency_phone=request.form.get(
                    'emergency_phone', '').strip() or None
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

            flash(
                f'Member {member.first_name} {member.last_name} registered successfully!', 'success')
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
    filter_date = request.args.get('date')
    filter_trainer = request.args.get('trainer')

    query = WorkoutSession.query

    # Filter by date
    if filter_date:
        try:
            filter_date_obj = datetime.strptime(filter_date, '%Y-%m-%d').date()
            query = query.filter(
                WorkoutSession.session_date == filter_date_obj)
        except ValueError:
            flash('Invalid date format', 'error')
    else:
        # Default to upcoming sessions only
        query = query.filter(WorkoutSession.session_date >= date.today())

    # Filter by trainer
    if filter_trainer:
        query = query.filter(WorkoutSession.trainer_id == int(filter_trainer))

    sessions = query.order_by(WorkoutSession.session_date, WorkoutSession.start_time).paginate(
        page=page, per_page=10, error_out=False
    )

    # Get all trainers for filter dropdown
    trainers = Trainer.query.all()
    members = Member.query.filter_by(status='active').all()

    return render_template('sessions/list.html',
                           sessions=sessions,
                           trainers=trainers,
                           members=members,
                           filter_date=filter_date,
                           filter_trainer=filter_trainer)


@app.route('/sessions/new', methods=['GET', 'POST'])
def new_session():
    """Create new workout session"""
    if request.method == 'POST':
        errors = []

        # Validation
        if not request.form.get('title', '').strip():
            errors.append('Session title is required')
        if not request.form.get('trainer_id'):
            errors.append('Please select a trainer')
        if not request.form.get('session_date'):
            errors.append('Session date is required')
        if not request.form.get('start_time'):
            errors.append('Start time is required')
        if not request.form.get('end_time'):
            errors.append('End time is required')

        # Date validation
        session_date = None
        if request.form.get('session_date'):
            try:
                session_date = datetime.strptime(
                    request.form['session_date'], '%Y-%m-%d').date()
                if session_date < date.today():
                    errors.append('Session date cannot be in the past')
            except ValueError:
                errors.append('Please enter a valid session date')

        # Time validation
        start_time = None
        end_time = None
        if request.form.get('start_time') and request.form.get('end_time'):
            try:
                start_time = datetime.strptime(
                    request.form['start_time'], '%H:%M').time()
                end_time = datetime.strptime(
                    request.form['end_time'], '%H:%M').time()
                if end_time <= start_time:
                    errors.append('End time must be after start time')
            except ValueError:
                errors.append('Please enter valid times in HH:MM format')

        # Capacity validation
        max_capacity = 10  # default
        if request.form.get('max_capacity'):
            try:
                max_capacity = int(request.form['max_capacity'])
                if max_capacity <= 0:
                    errors.append('Maximum capacity must be greater than 0')
                if max_capacity > 50:
                    errors.append('Maximum capacity cannot exceed 50')
            except ValueError:
                errors.append(
                    'Please enter a valid number for maximum capacity')

        if errors:
            for error in errors:
                flash(error, 'error')
            trainers = Trainer.query.all()
            return render_template('sessions/schedule.html', trainers=trainers)

        try:
            session = WorkoutSession(
                title=request.form['title'].strip(),
                description=request.form.get(
                    'description', '').strip() or None,
                trainer_id=int(request.form['trainer_id']),
                session_date=session_date,
                start_time=start_time,
                end_time=end_time,
                max_capacity=max_capacity
            )

            db.session.add(session)
            db.session.commit()

            flash(
                f'Session "{session.title}" scheduled successfully!', 'success')
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


@app.route('/members/import', methods=['GET', 'POST'])
def import_members():
    """Import members from CSV file"""
    if request.method == 'POST':
        file = request.files.get('file')

        if not file or not file.filename.endswith('.csv'):
            flash('Please upload a valid CSV file', 'error')
            return redirect(url_for('members'))

        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)

        # Skip header row
        next(csv_input)

        for row in csv_input:
            try:
                member = Member(
                    first_name=row[0].strip(),
                    last_name=row[1].strip(),
                    email=row[2].strip(),
                    phone=row[3].strip() or None,
                    date_of_birth=datetime.strptime(
                        row[4], '%Y-%m-%d').date() if row[4] else None,
                    gender=row[5] if row[5] else None,
                    emergency_contact=row[6].strip() or None,
                    emergency_phone=row[7].strip() or None
                )

                db.session.add(member)
                db.session.commit()

            except Exception as e:
                db.session.rollback()
                flash(
                    f'Error importing member {row[0]} {row[1]}: {str(e)}', 'error')

        flash('Members imported successfully!', 'success')
        return redirect(url_for('members'))

    return render_template('members/import.html')


@app.route('/members/export')
def export_members():
    """Export members to CSV"""
    try:
        # Create CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)

        # Write header
        writer.writerow([
            'ID', 'First Name', 'Last Name', 'Email', 'Phone',
            'Date of Birth', 'Gender', 'Status', 'Join Date',
            'Emergency Contact', 'Emergency Phone', 'Current Plan'
        ])

        # Write member data
        members = Member.query.all()
        for member in members:
            # Get current plan
            current_plan = None
            if member.member_plans:
                current_plan = member.member_plans[-1].plan.name

            writer.writerow([
                member.id,
                member.first_name,
                member.last_name,
                member.email,
                member.phone or '',
                member.date_of_birth or '',
                member.gender or '',
                member.status,
                member.created_at.strftime(
                    '%Y-%m-%d') if member.created_at else '',
                member.emergency_contact or '',
                member.emergency_phone or '',
                current_plan or ''
            ])

        # Create response
        output.seek(0)
        response = make_response(output.getvalue())
        response.headers['Content-Type'] = 'text/csv'
        response.headers[
            'Content-Disposition'] = f'attachment; filename=members_export_{date.today().strftime("%Y%m%d")}.csv'

        flash('Members exported successfully!', 'success')
        return response

    except Exception as e:
        flash(f'Error exporting members: {str(e)}', 'error')
        return redirect(url_for('members'))


@app.route('/sessions/export')
def export_sessions():
    """Export sessions to CSV"""
    try:
        # Create CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)

        # Write header
        writer.writerow([
            'ID', 'Title', 'Description', 'Trainer', 'Date',
            'Start Time', 'End Time', 'Max Capacity', 'Current Bookings',
            'Available Spots', 'Status'
        ])

        # Write session data
        sessions = WorkoutSession.query.order_by(
            WorkoutSession.session_date, WorkoutSession.start_time).all()
        for session in sessions:
            trainer_name = session.trainer.name if session.trainer else 'No Trainer'
            available_spots = session.max_capacity - session.current_bookings
            status = 'Full' if session.is_full else 'Available'

            writer.writerow([
                session.id,
                session.title,
                session.description or '',
                trainer_name,
                session.session_date,
                session.start_time,
                session.end_time,
                session.max_capacity,
                session.current_bookings,
                available_spots,
                status
            ])

        # Create response
        output.seek(0)
        response = make_response(output.getvalue())
        response.headers['Content-Type'] = 'text/csv'
        response.headers[
            'Content-Disposition'] = f'attachment; filename=sessions_export_{date.today().strftime("%Y%m%d")}.csv'

        flash('Sessions exported successfully!', 'success')
        return response

    except Exception as e:
        flash(f'Error exporting sessions: {str(e)}', 'error')
        return redirect(url_for('sessions'))


# API Routes for AJAX calls

@app.route('/api/members/<int:id>/toggle-status', methods=['POST'])
def toggle_member_status(id):
    """Toggle member status between active and inactive"""
    try:
        member = Member.query.get_or_404(id)
        member.status = 'inactive' if member.status == 'active' else 'active'
        db.session.commit()

        return jsonify({
            'success': True,
            'new_status': member.status,
            'message': f'Member status changed to {member.status}'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error updating member status: {str(e)}'
        }), 500


@app.route('/api/sessions/<int:id>/bookings')
def session_bookings(id):
    """Get session booking details"""
    try:
        session = WorkoutSession.query.get_or_404(id)
        bookings = SessionBooking.query.filter_by(session_id=id).all()

        booking_data = []
        for booking in bookings:
            booking_data.append({
                'id': booking.id,
                'member_name': f"{booking.member.first_name} {booking.member.last_name}",
                'member_email': booking.member.email,
                'booking_date': booking.created_at.strftime('%Y-%m-%d %H:%M') if booking.created_at else ''
            })

        return jsonify({
            'session_title': session.title,
            'total_capacity': session.max_capacity,
            'current_bookings': len(booking_data),
            'available_spots': session.max_capacity - len(booking_data),
            'bookings': booking_data
        })
    except Exception as e:
        return jsonify({
            'error': f'Error fetching session bookings: {str(e)}'
        }), 500


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
