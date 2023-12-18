from .. import schemas, models
from fastapi import Depends, HTTPException, status
from . import vocabulary
import random

def add_result(request: schemas.Test_result, db: Depends, current_user: schemas.TokenData):
    new_test_result = models.Test_result(total_question = request.total_question, result = request.result, user_id = current_user.id)
    db.add(new_test_result)
    db.commit()
    db.refresh(new_test_result)
    return new_test_result

def get_result(db: Depends, current_user: schemas.TokenData):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    return user.test_results

def get_test(total_question:int, db: Depends, current_user: schemas.TokenData):
    vocabularys = vocabulary.get_all_vocabulary(db, current_user)
    random.shuffle(vocabularys)
    if total_question > len(vocabularys):
        return vocabularys
    else:
        for i in range(len(vocabularys) - total_question):
            vocabularys.pop(-1)
        return vocabularys