from app.database.bd import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()