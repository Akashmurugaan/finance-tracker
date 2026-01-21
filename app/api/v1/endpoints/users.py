from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import get_current_active_user
from app.schemas.user import User, UserUpdate
from typing import List

router = APIRouter()

@router.get("/me", response_model=User)
def read_current_user(
    current_user: User = Depends(get_current_active_user)
):
    return current_user

@router.put("/me", response_model=User)
def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    from app.crud.user import update_user
    return update_user(db, current_user.id, user_update)