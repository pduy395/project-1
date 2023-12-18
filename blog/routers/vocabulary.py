from fastapi import APIRouter, Depends, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from . import oauth2
from sqlalchemy import and_, or_
from ..respository import vocabulary
from typing import List

router = APIRouter(
    prefix="/vocabulary",
    tags=['vocabulary'])

get_db = database.get_db

@router.post('/add/',status_code=status.HTTP_201_CREATED,)
async def add_vocabulary(request:schemas.Vocabulary, topic_id: int, db: Session = Depends(get_db)):
    return vocabulary.add_vocabulary(request,topic_id,db)


@router.get('/{topic_name}',)
async def get_vocabulary_in_topic(topic_name: str, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return vocabulary.get_vocabulary(topic_name,db,current_user)
    

@router.get('/', response_model=List[schemas.Vocabulary])
async def get_vocabulary(db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return vocabulary.get_all_vocabulary(db,current_user)
    
