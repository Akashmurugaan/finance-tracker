from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class UserProfileBase(BaseModel):
    phone_number: Optional[str] = None
    profile_picture: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = "USD"
    notification_enabled: Optional[bool] = True


class UserProfileUpdate(UserProfileBase):
    """Schema for updating user profile"""
    pass


class UserProfileCreate(UserProfileBase):
    """Schema for creating user profile"""
    user_id: int


class UserProfile(UserProfileBase):
    """Complete user profile schema"""
    id: int
    user_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


class UserProfileResponse(BaseModel):
    """Response schema with user and profile info"""
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    profile_picture: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = "USD"
    notification_enabled: Optional[bool] = True
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
