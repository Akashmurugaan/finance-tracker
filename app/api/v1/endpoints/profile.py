from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.crud.user_profile import (
    get_profile_by_user_id,
    update_profile,
    get_full_profile,
    get_or_create_profile,
)
from app.schemas.user_profile import UserProfileUpdate, UserProfile, UserProfileResponse
from app.dependencies import get_current_active_user

router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)


@router.get("/me", response_model=UserProfileResponse)
def get_my_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get current user's complete profile"""
    profile_data = get_full_profile(db, current_user.id)
    if not profile_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return profile_data


@router.get("/{user_id}", response_model=UserProfileResponse)
def get_user_profile(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get user profile by user ID (public endpoint)"""
    profile_data = get_full_profile(db, user_id)
    if not profile_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return profile_data


@router.put("/me", response_model=UserProfileResponse)
def update_my_profile(
    profile_update: UserProfileUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update current user's profile"""
    updated_profile = update_profile(db, current_user.id, profile_update)
    if not updated_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update profile"
        )
    
    profile_data = get_full_profile(db, current_user.id)
    return profile_data


@router.patch("/me", response_model=UserProfileResponse)
def partial_update_my_profile(
    profile_update: UserProfileUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Partially update current user's profile (PATCH)"""
    updated_profile = update_profile(db, current_user.id, profile_update)
    if not updated_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update profile"
        )
    
    profile_data = get_full_profile(db, current_user.id)
    return profile_data
