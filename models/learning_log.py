from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.base import Base

class LearningLog(Base):
    __tablename__ = 'learning_logs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date_completed = Column(Date)

    skill_id = Column(Integer, ForeignKey('skills.id'))
    skill = relationship("Skill", back_populates="logs")

    def __repr__(self):
        return f"<LearningLog(title='{self.title}', date={self.date_completed})>"
