from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/frauddb"
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@host.docker.internal:5432/frauddb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)