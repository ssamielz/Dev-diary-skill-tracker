from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)  # e.g., Beginner, Intermediate, Advanced

    logs = relationship("LearningLog", back_populates="skill", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Skill(name='{self.name}', level='{self.level}')>"
