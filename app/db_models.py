from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class TransactionRecord(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    features = Column(JSONB)

    prediction = Column(Integer)

    probability = Column(Float)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())