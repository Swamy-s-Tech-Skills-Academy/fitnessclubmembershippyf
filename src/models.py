# Database Models for Fitness Club Membership System
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    """Member model for storing member information"""
    __tablename__ = 'members'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    emergency_contact = db.Column(db.String(100))
    emergency_phone = db.Column(db.String(20))
    join_date = db.Column(db.Date, default=date.today)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    member_plans = db.relationship('MemberPlan', backref='member', lazy=True)
    session_bookings = db.relationship('SessionBooking', backref='member', lazy=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None
    
    def __repr__(self):
        return f'<Member {self.full_name}>'

class MembershipPlan(db.Model):
    """Membership plan model for different subscription tiers"""
    __tablename__ = 'membership_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    monthly_price = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    member_plans = db.relationship('MemberPlan', backref='plan', lazy=True)
    
    def __repr__(self):
        return f'<MembershipPlan {self.name}>'

class MemberPlan(db.Model):
    """Junction table for member and membership plan relationship"""
    __tablename__ = 'member_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('membership_plans.id'), nullable=False)
    start_date = db.Column(db.Date, default=date.today)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')
    
    def __repr__(self):
        return f'<MemberPlan {self.member.full_name} - {self.plan.name}>'

class Trainer(db.Model):
    """Trainer model for workout session instructors"""
    __tablename__ = 'trainers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    workout_sessions = db.relationship('WorkoutSession', backref='trainer', lazy=True)
    
    def __repr__(self):
        return f'<Trainer {self.name}>'

class WorkoutSession(db.Model):
    """Workout session model for scheduled fitness classes"""
    __tablename__ = 'workout_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))
    session_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    max_capacity = db.Column(db.Integer, default=10)
    current_bookings = db.Column(db.Integer, default=0)
    
    # Relationships
    session_bookings = db.relationship('SessionBooking', backref='session', lazy=True)
    
    @property
    def available_spots(self):
        return self.max_capacity - self.current_bookings
    
    @property
    def is_full(self):
        return self.current_bookings >= self.max_capacity
    
    def __repr__(self):
        return f'<WorkoutSession {self.title} on {self.session_date}>'

class SessionBooking(db.Model):
    """Session booking model for member workout reservations"""
    __tablename__ = 'session_bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('workout_sessions.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='confirmed')
    
    def __repr__(self):
        return f'<SessionBooking {self.member.full_name} - {self.session.title}>'
