from sqlalchemy.orm import Session
from app.models.user_profile import UserProfile
from app.models.user import User
from app.schemas.user_profile import UserProfileCreate, UserProfileUpdate
from typing import Optional


def get_or_create_profile(db: Session, user_id: int) -> UserProfile:
    """Get existing profile or create a new one"""
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        profile = UserProfile(user_id=user_id)
        db.add(profile)
        db.commit()
        db.refresh(profile)
    return profile


def get_profile_by_user_id(db: Session, user_id: int) -> Optional[UserProfile]:
    """Get user profile by user ID"""
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()


def create_profile(db: Session, user_id: int) -> UserProfile:
    """Create a new user profile"""
    profile = UserProfile(user_id=user_id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def update_profile(db: Session, user_id: int, profile_update: UserProfileUpdate) -> Optional[UserProfile]:
    """Update user profile"""
    profile = get_or_create_profile(db, user_id)
    
    update_data = profile_update.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    return profile


def get_full_profile(db: Session, user_id: int) -> Optional[dict]:
    """Get complete profile information (user + profile details)"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    
    profile = get_or_create_profile(db, user_id)
    
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
        "phone_number": profile.phone_number,
        "profile_picture": profile.profile_picture,
        "bio": profile.bio,
        "date_of_birth": profile.date_of_birth,
        "address": profile.address,
        "city": profile.city,
        "country": profile.country,
        "currency": profile.currency,
        "notification_enabled": profile.notification_enabled,
    }


def delete_profile(db: Session, user_id: int) -> bool:
    """Delete user profile"""
    profile = get_profile_by_user_id(db, user_id)
    if profile:
        db.delete(profile)
        db.commit()
        return True
    return False
