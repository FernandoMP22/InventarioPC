from sqlalchemy.orm import Session, sessionmaker

from backend.database.conexion_sqlalchemy import engine


SessionLocal = sessionmaker(
    bind=engine
)


def get_db():
    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()