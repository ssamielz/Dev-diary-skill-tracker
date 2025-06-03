import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.skill import Skill
from models.learning_log import LearningLog
from models.base import Base

# Set up DB session
engine = create_engine('sqlite:///skill_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

def menu():
    print("\n==== SKILL TRACKER CLI ====")
    print("1. Create a Skill")
    print("2. View All Skills")
    print("3. Delete a Skill")
    print("4. Log Learning Progress")
    print("5. View Learning Logs")
    print("6. Exit")

def create_skill():
    name = input("Skill name: ").strip()
    level = input("Proficiency level (e.g., Beginner, Intermediate, Pro): ").strip()
    if not name or not level:
        print("Name and level are required.")
        return
    skill = Skill(name=name, level=level)
    session.add(skill)
    session.commit()
    print(f"Skill '{name}' added.")

def view_skills():
    skills = session.query(Skill).all()
    if not skills:
        print("No skills found.")
    for skill in skills:
        print(f"[{skill.id}] {skill.name} - {skill.level}")

def delete_skill():
    view_skills()
    try:
        skill_id = int(input("Enter Skill ID to delete: "))
        skill = session.get(Skill, skill_id)
        if skill:
            session.delete(skill)
            session.commit()
            print(f"Skill '{skill.name}' deleted.")
        else:
            print("Skill not found.")
    except ValueError:
        print("Invalid input. Enter a number.")


def log_learning():
    view_skills()
    try:
        skill_id = int(input("Skill ID: "))
        skill = session.get(Skill, skill_id)
        if not skill:
            print("Skill not found.")
            return
        title = input("Log title: ").strip()
        description = input("What did you learn?: ").strip()
        date_input = input("Date completed (YYYY-MM-DD): ").strip()
        date_completed = datetime.strptime(date_input, "%Y-%m-%d").date()

        log = LearningLog(
            title=title,
            description=description,
            date_completed=date_completed,
            skill=skill
        )
        session.add(log)
        session.commit()
        print(f"Log added for '{skill.name}'.")
    except ValueError:
        print("Invalid input or date format.")


def view_logs():
    logs = session.query(LearningLog).all()
    if not logs:
        print("No logs found.")
    for log in logs:
        print(f"[{log.id}] {log.title} ({log.date_completed}) - Skill: {log.skill.name}")

def run():
    while True:
        menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            create_skill()
        elif choice == "2":
            view_skills()
        elif choice == "3":
            delete_skill()
        elif choice == "4":
            log_learning()
        elif choice == "5":
            view_logs()
        elif choice == "6":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()
