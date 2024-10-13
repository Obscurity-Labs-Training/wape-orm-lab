from database import Base, engine
from models import User, Book

def create_database():
    print("Creating database...")
    Base.metadata.create_all(bind=engine)
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
