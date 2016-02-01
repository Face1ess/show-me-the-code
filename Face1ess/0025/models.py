from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(60))
    
    def __init__(self,task=None):
        self.task = task
    
    def __repr__(self):
        return '<Task %s>' % (self.task)
