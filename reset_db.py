#!/usr/bin/env python
"""Reset the database - drop and recreate tables"""

from app.core.database import engine, Base
from app.models.user import User
from sqlalchemy import text

print("=" * 50)
print("Database Reset")
print("=" * 50)

# Drop the users table if it exists
with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS users CASCADE"))
    connection.commit()
    print("✓ Dropped users table")

# Create all tables
Base.metadata.create_all(bind=engine)
print("✓ Created fresh tables")

print("\n✓ Database reset complete!")
