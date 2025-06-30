# 🚀 Live Coding Quick Reference Guide

## ⏰ **TIMING BREAKDOWN**

- **Pre-Sprint Setup**: 5 minutes
- **Sprint 1 (Backend)**: 15 minutes
- **Sprint 2 (Frontend)**: 15 minutes
- **Sprint 3 (Polish)**: 15 minutes
- **Total**: 50 minutes

## 📋 **PROMPT CHECKLIST**

### ✅ Pre-Sprint Setup

- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Folder structure ready

### ✅ Sprint 1 - Backend

- [ ] Models created (6 tables)
- [ ] Flask app with routes
- [ ] Database initialized
- [ ] Sample data loaded

### ✅ Sprint 2 - Frontend

- [ ] Base template with navigation
- [ ] Dashboard with analytics
- [ ] Member management pages
- [ ] Session booking interface

### ✅ Sprint 3 - Integration

- [ ] Form validation added
- [ ] CSV export working
- [ ] AJAX endpoints functional
- [ ] Production polish complete

## 🎯 **KEY VALIDATION POINTS**

After each sprint, test:

**Sprint 1**: `http://localhost:5000` shows dashboard
**Sprint 2**: All pages load with Tailwind styling
**Sprint 3**: Forms validate, CSV exports work

## 🔧 **TROUBLESHOOTING**

### Common Issues:

- **Import errors**: Check virtual environment is activated
- **Template errors**: Verify folder structure in src/templates/
- **Database issues**: Delete instance/fitness_club.db and re-run init_db.py

### Quick Fixes:

```bash
# Restart virtual environment
.venv\Scripts\activate

# Recreate database
cd src
rm instance/fitness_club.db
python init_db.py
```

## 📂 **FINAL PROJECT STRUCTURE**

```
fitness-club/
├── .venv/
├── requirements.txt
├── src/
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   ├── init_db.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── members/
│   │   ├── plans/
│   │   └── sessions/
│   └── instance/
│       └── fitness_club.db
├── tests/
├── docs/
└── prompts/
```

## 🎬 **DEMO SCRIPT**

1. **Opening**: "Building a fitness club system in 45 minutes"
2. **Sprint 1**: Show database models and API endpoints
3. **Sprint 2**: Demonstrate responsive design and navigation
4. **Sprint 3**: Export CSV, show form validation
5. **Wrap-up**: Complete working application demo
