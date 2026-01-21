#!/usr/bin/env python
"""Test database setup and create tables"""

from app.core.database import engine, Base, SessionLocal
from app.models.user import User
from sqlalchemy import inspect

print("=" * 50)
print("Database Setup Test")
print("=" * 50)

# Create all tables
Base.metadata.create_all(bind=engine)
print("✓ Tables created successfully")

# Check what tables exist
inspector = inspect(engine)
tables = inspector.get_table_names()
print(f"\n✓ Tables in database: {tables}")

# Check users table structure
if 'users' in tables:
    columns = inspector.get_columns('users')
    print("\n✓ Users table columns:")
    for col in columns:
        print(f"  - {col['name']}: {col['type']}")

# Check if any users exist
db = SessionLocal()
try:
    user_count = db.query(User).count()
    print(f"\n✓ Users in database: {user_count}")
finally:
    db.close()

print("\n✓ Database setup verified!")
