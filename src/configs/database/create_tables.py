from configs.database.db import Base, engine

# Import All The Tables Here


def create_tables():
    Base.metadata.create_all(bind=engine)
