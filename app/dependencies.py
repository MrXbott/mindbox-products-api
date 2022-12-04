from .db import SessionLocal, engine


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()