from .database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__="user_account"
    id = Column(Integer, primary_key=True,index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)

    topics = relationship("Topic", back_populates="creator")
    test_results = relationship("Test_result", back_populates="creator")
    progresses = relationship("Progress", back_populates="creator")

class Topic(Base):
    __tablename__="topic"
    id = Column(Integer, primary_key=True,index=True)
    topic_name = Column(String)
    user_id = Column(Integer,ForeignKey("user_account.id"))

    creator = relationship("User", back_populates="topics")
    vocabularys = relationship("Vocabulary", back_populates="owner")

class Vocabulary(Base):
    __tablename__="vocabulary"
    id = Column(Integer, primary_key=True,index=True)
    word = Column(String)
    meaning = Column(String)
    type = Column(String)
    topic_id = Column(Integer,ForeignKey("topic.id"))

    owner = relationship("Topic", back_populates="vocabularys")


class Test_result(Base):
    __tablename__="test_result"
    id = Column(Integer, primary_key=True,index=True)
    total_question = Column(Integer)
    result = Column(Integer)
    user_id = Column(Integer,ForeignKey("user_account.id"))

    creator = relationship("User", back_populates="test_results")

class Progress(Base):
    __tablename__ = "progress"
    id = Column(Integer, primary_key=True,index=True)
    progress = Column(Integer)
    user_id = Column(Integer,ForeignKey("user_account.id"))
    topic_id = Column(Integer,ForeignKey("topic.id"))

    creator = relationship("User", back_populates="progresses")
