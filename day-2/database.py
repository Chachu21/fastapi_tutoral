from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase
from config import settings

# ============================
# Engine creation
# ============================
# pool_pre_ping=True checks if connection is alive (prevents stale connection errors)
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,        # optional: logs SQL queries if DEBUG=True
    pool_pre_ping=True
)

# ============================
# Session factory
# ============================
# Use this session for all DB operations
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ============================
# Base class for models
# ============================
class Base(DeclarativeBase):
    pass

# ============================
# Dependency for FastAPI endpoints
# ============================
def get_db():
    """
    Yield a database session for a request and close it after.
    Automatically rolls back in case of errors.
    """
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
