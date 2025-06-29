# 🏋️‍♂️ Fitness Club Membership System

A comprehensive full-stack fitness club membership management system built with **Python Flask**, **Tailwind CSS**, and **SQLite**. Designed to streamline member management, plan subscriptions, and workout scheduling for fitness clubs of any size.

## ✨ Features

### 👥 Member Management

- **Member Registration** - Complete signup with personal details and emergency contacts
- **Profile Management** - View, edit, and update member information
- **Member Search** - Find members by name, email, or phone number
- **Status Tracking** - Active, inactive, and suspended member states

### 📋 Membership Plans

- **Flexible Plans** - Basic ($29/month), Pro ($49/month), Elite ($79/month)
- **Plan Assignment** - Easy plan switching and management
- **Billing Cycles** - Monthly, quarterly, and annual options
- **Feature Management** - Different access levels per plan

### 🗓️ Workout Sessions

- **Session Scheduling** - Book classes by date, time, and trainer
- **Trainer Management** - Manage trainer profiles and specializations
- **Capacity Control** - Set maximum participants per session
- **Session History** - Track completed and upcoming workouts

### 🎨 Modern UI/UX

- **Responsive Design** - Mobile-first Tailwind CSS layout
- **Intuitive Navigation** - Clean, user-friendly interface
- **Form Validation** - Real-time validation with helpful error messages
- **Dashboard Overview** - Quick stats and recent activity

## 🛠️ Tech Stack

| Component    | Technology                      |
| ------------ | ------------------------------- |
| **Backend**  | Python Flask                    |
| **Frontend** | HTML5, Tailwind CSS, JavaScript |
| **Database** | SQLite                          |
| **Styling**  | Tailwind CSS                    |
| **Forms**    | WTForms (Flask-WTF)             |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ installed on your system
- Basic knowledge of Flask and HTML

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/fitness-club-membership.git
   cd fitness-club-membership
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**

   ```bash
   python database.py
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📊 Database Schema

The system uses SQLite with the following main tables:

- **members** - Member personal information and status
- **membership_plans** - Available subscription plans
- **member_plans** - Plan assignments and billing
- **trainers** - Trainer profiles and specializations
- **workout_sessions** - Scheduled fitness classes
- **session_bookings** - Member session reservations

## 🎯 Usage Examples

### Register a New Member

1. Navigate to "Add Member"
2. Fill in personal details and emergency contact
3. Select membership plan
4. Submit form to create account

### Schedule a Workout Session

1. Go to "Schedule Sessions"
2. Select date, time, and trainer
3. Set session type and capacity
4. Save session for member booking

### Book a Session

1. View available sessions
2. Select desired workout
3. Confirm booking
4. Receive confirmation

## 🔧 Configuration

Edit `config.py` to customize:

```python
class Config:
    SECRET_KEY = 'your-secret-key-here'
    DATABASE_URL = 'sqlite:///fitness_club.db'
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file upload
```

## 📈 Development Roadmap

### Phase 1 ✅

- [x] Basic member CRUD operations
- [x] Membership plan management
- [x] Simple session scheduling

### Phase 2 🚧

- [ ] Payment integration (Stripe)
- [ ] Email notifications
- [ ] Advanced reporting
- [ ] Member check-in system

### Phase 3 📋

- [ ] Mobile app companion
- [ ] Equipment booking
- [ ] Nutrition tracking
- [ ] Social features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check `/docs` folder for detailed guides
- **Issues**: Report bugs on GitHub Issues
- **Contact**: fitness-club-support@example.com

## 🙏 Acknowledgments

- Built for educational purposes and learning Flask development
- Tailwind CSS for beautiful, responsive styling
- SQLite for simple, reliable data storage
- Flask community for excellent documentation

---

**Happy Coding! 🏋️‍♀️** Start building your fitness club management system today!
