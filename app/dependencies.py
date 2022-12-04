from .db import SessionLocal, engine

from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()