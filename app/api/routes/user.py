from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud import user as user_crud
from app.api.dependencies.db import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=list[UserOut])
async def get_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db)

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user(db, user_id)

@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.update_user(db, user_id, user)

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.delete_user(db, user_id)
