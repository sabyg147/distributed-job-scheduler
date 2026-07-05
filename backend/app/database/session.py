from sqlalchemy.orm import sessionmaker

from app.database.database import engine


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Dependency used by FastAPI routes.

    Creates one database session
    for every request.

    Closes automatically.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()