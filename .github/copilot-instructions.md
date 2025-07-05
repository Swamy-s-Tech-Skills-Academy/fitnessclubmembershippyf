# 🤖 GitHub Copilot Instructions: Fitness Club Membership System

Welcome to the **Fitness Club Membership System** – a 45-minute live coding demo using **Flask**, **Tailwind CSS**, **Font Awesome**, **Google Fonts**, and **SQLite**. This project is structured into sprints with clear instructions to help GitHub Copilot Agent provide contextual suggestions aligned with the development flow.

---

## 📦 Project Summary

| Key Detail         | Value                      |
| ------------------ | -------------------------- |
| Language           | Python                     |
| Backend Framework  | Flask                      |
| ORM                | SQLAlchemy                 |
| Forms Library      | Flask-WTF                  |
| Frontend Framework | Tailwind CSS (CDN)         |
| Icons              | Font Awesome (CDN)         |
| Typography         | Google Fonts (CDN)         |
| Database           | SQLite (in `src/instance`) |
| Mode               | Live coding demo           |
| Duration           | ~45 minutes                |

---

## 📁 Project Structure (Expected)

**Starter Project Includes:**

- A. `.copilot/settings.json` - GitHub Copilot configuration
- B. `.github/copilot-instructions.md` - Copilot Agent instructions
- C. `docs/` folder - Documentation and images
- D. `prompts/` folder - All sprint `.md` files with copy-paste prompts
- E. `.gitignore` - Python/Flask optimized ignore rules
- F. `LICENSE` - Project license
- G. `README.md` - Project documentation
- H. `requirements.txt` - All Python dependencies with versions

**Generated During Development:**

```
src\
├── app.py
├── config.py
├── init_db.py
├── models.py
├── templates\
├── static\
└── instance\
```

---

## � Coding Standards

- `camelCase` → variables, functions
- `PascalCase` → class and component names
- `ALL_CAPS` → constants
- `_prefix` → private class members
- Prefer explicit error handling (`try/except`)
- Use contextual logging for debugging

---

## 🧠 Contextual Path Awareness

Copilot Agent must remember:

- The project structure is focused on development with Flask app in `src\` folder
- All application code resides in the `src\` directory
- Database files are stored in `src\instance\`
- Templates are in `src\templates\` and static files in `src\static\`
- Use Windows path separators (\) in commands and file paths

---

## 🚦 Workflow and Sprint Files

### 🛠 Sprint Files (Sequential)

| Sprint Step | File Name                  | Duration | Summary                                         |
| ----------- | -------------------------- | -------- | ----------------------------------------------- |
| 1️⃣          | `2_Pre-Sprint-Setup.md`    | 5 min    | Setup virtual env, Flask, CDN resources         |
| 2️⃣          | `3_Sprint1-Backend.md`     | 15 min   | SQLAlchemy models & routes                      |
| 3️⃣          | `4_Sprint2-Frontend.md`    | 15 min   | Templates, Tailwind, FA icons, Google Fonts     |
| 4️⃣          | `5_Sprint3-Integration.md` | 15 min   | AJAX, validation, CSV export, production polish |

### 📚 Reference Files

_Note: Reference files have been removed to focus on core sprint workflow_

---

## ⚙️ Copilot Agent Expectations

Copilot Agent should:

- Follow file flow: `2_`, `3_`, `4_`, `5_`
- Suggest model creation using SQLAlchemy
- Recommend routes/views using Flask decorators
- Generate Tailwind-based HTML templates with Font Awesome icons
- Integrate Google Fonts typography (Inter for body, Poppins for headings)
- Propose Flask-WTF forms with comprehensive validation
- Generate JavaScript/AJAX functionality for dynamic interactions
- Use PowerShell `@"..."@` format for writing files (Windows-optimized)
- Follow `settings.json` configuration
- Focus on development workflow (no test file generation)
- Use Windows path separators (\) and PowerShell commands

---

## ✅ Deliverables by End

- Fully working Flask web app
- CRUD + booking features with relationships
- Professional UI with TailwindCSS, Font Awesome icons, and Google Fonts
- Data export capability
- Clean, modular source layout
- Browser-testable endpoints

---

## 🔁 Developer Commands (For Manual Verification)

### **Windows PowerShell:**

```powershell
# Setup (performed by user, not Copilot)
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Run database init
Set-Location src
python init_db.py

# Start app
python app.py
# Open: <http://localhost:5000>
```

> **Note**: These commands are for user verification after Copilot generates the code. The starter project includes all configuration files: `.gitignore`, `requirements.txt`, `.copilot/settings.json`, `.github/copilot-instructions.md`, `docs/`, `prompts/`, `LICENSE`, and `README.md`.

---

## 💡 Reminder to Copilot Agent

If the user invokes a prompt:

- Identify the current sprint file (based on file name)
- Generate or complete relevant code
- Respect coding standards and folder structure
- Provide context-aware completions, not global changes
- **Do not move to the next sprint unless the user (Swamy) confirms the current sprint is complete and correct**

### 🧪 Sprint Review Process (Agile-style)

Copilot should:

1. **Generate code for the current sprint**
2. **Wait for Swamy to test and validate**
3. **Incorporate any feedback**
4. **Proceed to the next sprint only after Swamy explicitly agrees**

This ensures quality, clarity, and a smooth live demo flow.

---

## 📂 Folder Purpose Clarification

### 💡 `prompts/` – Sprint Prompts for Copilot Agent

- Contains `.md` prompt files used **exclusively** for **coding guidance during live sprints**.
- Copilot should **rely only on files inside `prompts/`** for generating code during the live demo.
- Each file is self-contained, follows the naming pattern `2_`, `3_`, `4_`, etc.
- Focus on development workflow and live coding demonstrations.

---
