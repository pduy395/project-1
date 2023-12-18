from .. import schemas, models
from fastapi import Depends, HTTPException, status
from sqlalchemy import and_ , or_
from typing import List

def user_create_topic(request: schemas.Topic, db: Depends, current_user: schemas.TokenData):
    new_topic = models.Topic(topic_name = request.topic_name, user_id = current_user.id)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

def create_topic(request: schemas.Topic, db: Depends, ):
    new_topic = models.Topic(topic_name = request.topic_name, user_id = None)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

def get_all_topic(db: Depends, current_user: schemas.TokenData):
    topics = db.query(models.Topic).filter(or_(models.Topic.user_id == None, models.Topic.user_id == current_user.id)).all()
    return topics

def destroy_topic(topic_name: str, db: Depends, current_user: schemas.TokenData):
    topics = db.query(models.Topic).filter(and_(models.Topic.user_id == current_user.id , models.Topic.topic_name == topic_name))
    if not topics.all() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    topics.delete()
    db.commit()
    return  

def get_progress(db: Depends, current_user: schemas.TokenData):
    progress = db.query(models.Progress).filter( models.Progress.user_id == current_user.id).all()
    return progress


def post_progress(request: schemas.Progress, db: Depends, current_user: schemas.TokenData):
    new_progress = models.Progress(progress = request.progress,user_id =current_user.id,topic_id = request.topic_id)
    db.add(new_progress)
    db.commit()
    db.refresh(new_progress)
    return new_progress