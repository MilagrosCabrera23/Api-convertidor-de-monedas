from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, last_name=user.last_name, age=user.age, adress=user.adress, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 300):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def get_user_by_last_name(db: Session, last_name: str):
    return db.query(User).filter(User.last_name == last_name).first()


def get_user_by_age(db: Session, age: int):
    return db.query(User).filter(User.age == age).first()


def get_user_by_adress(db: Session, adress: str):
    return db.query(User).filter(User.adress == adress).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.last_name = user.last_name
    db_user.age = user.age
    db_user.adress = user.adress
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
