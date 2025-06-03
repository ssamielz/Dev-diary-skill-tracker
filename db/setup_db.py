
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.skill import Skill
from models.learning_log import LearningLog

# Create SQLite database
engine = create_engine('sqlite:///skill_tracker.db')

# Bind the engine to the session
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

print("Database and tables created!")
