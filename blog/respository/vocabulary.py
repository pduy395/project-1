from fastapi import Depends, status, HTTPException
from .. import schemas, models
from sqlalchemy import or_, and_

def add_vocabulary(request: schemas.Vocabulary, topic_id: int, db: Depends):
    new_vocabulary = models.Vocabulary(word= request.word, meaning= request.meaning, type= request.type, topic_id= topic_id)
    db.add(new_vocabulary)
    db.commit()
    db.refresh(new_vocabulary)
    return new_vocabulary

def get_vocabulary(topic_name: str, db: Depends, current_user: schemas.TokenData):
    topics =db.query(models.Topic).filter(or_( models.Topic.user_id == None, models.Topic.user_id == current_user.id)).all()
    for topic in topics:
        if topic.topic_name == topic_name:
            return topic.vocabularys
    return 'not found'

def get_all_vocabulary(db: Depends, current_user: schemas.TokenData):
    topics =db.query(models.Topic).filter(or_( models.Topic.user_id == None, models.Topic.user_id == current_user.id)).all()
    vocabularys =[]
    for topic in topics:
        for vocabulary in topic.vocabularys:
            vocabularys.append(vocabulary)
    return vocabularys  

