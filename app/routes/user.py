from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from models.user import User


router = APIRouter()







@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()