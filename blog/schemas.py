from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    email: str
    password: str

class Topic(BaseModel):
    topic_name: str

class Vocabulary(BaseModel):
    word: str
    meaning: str
    type: str
    class Config():
        orm_mode = True

class Test_result(BaseModel):
    total_question: int
    result: int
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    user_name: str
    email: str
    class Config():
        orm_mode = True

class Login(BaseModel):
    user_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int| None = None

class Topic(BaseModel):
    topic_name: str


class Progress(BaseModel):
    progress: int
    topic_id: int

