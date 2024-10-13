from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Book

def get_session():
    return SessionLocal()

def create_user(name: str):
    session = get_session()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    print(f"User created: {new_user}")
    session.close()

def create_book(title: str, user_id: int):
    session = get_session()
    new_book = Book(title=title, user_id=user_id)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    print(f"Book created: {new_book}")
    session.close()

def read_users():
    session = get_session()
    users = session.query(User).all()
    for user in users:
        print(f"User: {user.name}")
        for book in user.books:
            print(f"  Book: {book.title}")
    session.close()

def update_book(book_id: int, new_title: str):
    session = get_session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = new_title
        session.commit()
        print(f"Book updated: {book}")
    else:
        print("Book not found.")
    session.close()

def delete_user(user_id: int):
    session = get_session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User deleted: {user.name}")
    else:
        print("User not found.")
    session.close()

if __name__ == "__main__":
    create_user("Alice")
    create_user("Bob")
    create_book("Alice's Adventures", 1)
    create_book("Bob's Guide to SQL", 2)

    print("\nUsers and their books:")
    read_users()

    update_book(1, "Alice's Updated Adventures")
    delete_user(2)
