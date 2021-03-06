from sqlalchemy import Table, Column, Integer, ForeignKey,String, Date
from sqlalchemy.orm import relationship, backref


from datetime import datetime
from config import *

# methods to initalize database and have it up and running 


def init_db():
    Base.metadata.create_all(bind=engine)


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(50))
    children = relationship("Short")

    def __init__(self,email=None,pwd = None):
        self.name = email
        self.email = email
        self.password = pwd
        

    def __repr__(self):
        return self.name



class Short(Base):
    __tablename__ = 'shorts'
    id = Column(Integer, primary_key=True)
    shorturl = Column(String(50), unique=True)
    longurl = Column(String(120), unique=True)
    created = Column(Date,default=datetime.utcnow)
    created_by = Column(Integer,ForeignKey('user.id'))

    def __init__(self,shorturl, longurl):
        self.shorturl = shorturl
        self.longurl = longurl
        

    def __repr__(self):
        return self.shorturl+' '+self.longurl

    
    