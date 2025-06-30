# 📁 Prompts Folder Organization

## 🎯 **PRIMARY PROMPT FILES** (Use These for Live Coding)

### **For 45-Minute Live Session:**

1. **[master-prompts.md](master-prompts.md)** - ⭐ **MAIN FILE** - All prompts in one document
2. **[00-pre-sprint-setup.md](00-pre-sprint-setup.md)** - Environment setup (5 min)
3. **[sprint1-backend-prompt.md](sprint1-backend-prompt.md)** - Backend development (15 min)
4. **[sprint2-frontend-prompt.md](sprint2-frontend-prompt.md)** - Frontend templates (15 min)
5. **[sprint3-integration-prompt.md](sprint3-integration-prompt.md)** - Integration & polish (15 min)

### **Reference Files:**

- **[README.md](README.md)** - Prompt collection overview
- **[quick-reference.md](quick-reference.md)** - Quick validation checklist

## 🚀 **RECOMMENDED USAGE**

### **Option 1: Single File Approach**

Use **[master-prompts.md](master-prompts.md)** - contains all prompts in proper sequence

### **Option 2: Individual Sprint Files**

Use individual sprint files for copy-pasting specific prompts during live coding

## 📋 **VALIDATION COMMANDS**

After each sprint:

**Pre-Sprint:**

```bash
.venv\Scripts\activate
```

**Sprint 1:**

```bash
cd src && python init_db.py && python app.py
# Visit http://localhost:5000
```

**Sprint 2:**

```bash
cd src && python app.py
# Test all pages load with styling
```

**Sprint 3:**

```bash
cd src && python app.py
# Test all features: forms, exports, validation
```

## 🎬 **For Live Coding Sessions**

1. **Preparation**: Review [master-prompts.md](master-prompts.md)
2. **Session**: Copy-paste prompts in sequence
3. **Reference**: Use [quick-reference.md](quick-reference.md) for timing
4. **Backup**: Individual sprint files if needed

## ⏰ **Timing**

- Pre-Sprint: 5 minutes
- Sprint 1: 15 minutes
- Sprint 2: 15 minutes
- Sprint 3: 15 minutes
- **Total: 50 minutes**
