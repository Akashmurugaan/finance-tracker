#!/usr/bin/env python
"""
Test script to demonstrate the complete user profile flow:
1. Register a user
2. Login to get token
3. Get profile
4. Update profile with additional details
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/finance-tracker"

# Test data
test_user = {
    "email": "john@example.com",
    "username": "john_doe",
    "password": "securepassword123",
    "full_name": "John Doe"
}

profile_update = {
    "phone_number": "+1-555-0123",
    "bio": "Finance enthusiast and tracker",
    "address": "123 Main Street",
    "city": "New York",
    "country": "USA",
    "currency": "USD",
    "notification_enabled": True
}

print("=" * 70)
print("USER PROFILE API TEST")
print("=" * 70)

# Step 1: Register
print("\n1️⃣  REGISTERING USER...")
response = requests.post(f"{BASE_URL}/auth/register", json=test_user)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    user_data = response.json()
    print(f"✓ User registered: {user_data['username']} ({user_data['email']})")
else:
    print(f"❌ Error: {response.text}")
    exit(1)

# Step 2: Login
print("\n2️⃣  LOGGING IN...")
login_data = {"username": test_user["username"], "password": test_user["password"]}
response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    token_data = response.json()
    token = token_data["access_token"]
    print(f"✓ Login successful")
    print(f"✓ Token: {token[:20]}...")
else:
    print(f"❌ Error: {response.text}")
    exit(1)

# Step 3: Get initial profile (no extra details yet)
print("\n3️⃣  GET INITIAL PROFILE...")
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{BASE_URL}/profile/me", headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    profile = response.json()
    print("✓ Current Profile:")
    print(json.dumps(profile, indent=2, default=str))
else:
    print(f"❌ Error: {response.text}")

# Step 4: Update profile with additional details
print("\n4️⃣  UPDATING PROFILE WITH DETAILS...")
response = requests.put(f"{BASE_URL}/profile/me", json=profile_update, headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    updated_profile = response.json()
    print("✓ Profile updated successfully!")
    print(json.dumps(updated_profile, indent=2, default=str))
else:
    print(f"❌ Error: {response.text}")

# Step 5: Get updated profile
print("\n5️⃣  GET UPDATED PROFILE...")
response = requests.get(f"{BASE_URL}/profile/me", headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    final_profile = response.json()
    print("✓ Final Profile:")
    print(json.dumps(final_profile, indent=2, default=str))
else:
    print(f"❌ Error: {response.text}")

print("\n" + "=" * 70)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 70)
print("\n📝 AVAILABLE ENDPOINTS:")
print("  GET  /finance-tracker/profile/me         - Get your profile")
print("  PUT  /finance-tracker/profile/me         - Update your profile")
print("  PATCH /finance-tracker/profile/me        - Partially update your profile")
print("  GET  /finance-tracker/profile/{user_id}  - Get any user's profile")
