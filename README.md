# 🧠 Dev Diary Skill Tracker

A command-line Python application that helps you track your programming skill development and learning progress over time.

## 📋 Features

- Add new skills you're working on
- Record daily/weekly learning logs tied to each skill
- View all skills and logs
- Delete skills if you're no longer focusing on them
- Simple CLI interface for interacting with your data

## 🛠 Tech Stack

- Python 3.8+
- SQLAlchemy ORM (2.0 syntax)
- SQLite database
- CLI interface


## 🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd Dev-diary-skill-tracker

2. **Setup virtual env**
    pipenv install
    pipenv shell

3. **Initialize db**
    python db/setup_db.py

4. **Run the app**
    python cli/main.py
