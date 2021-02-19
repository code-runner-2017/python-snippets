# ORM with SQLAlchemy (Flask)
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
#
# pip install Flask-SQLAlchemy flask-marshmallow marshmallow-sqlalchemy marshmallow

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# echo=True shows all SQL commands
engine = create_engine('sqlite:///:memory:', echo=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # String representation
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine) 
    session = Session()
    ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    session.add(ed_user)
    our_user = session.query(User).filter_by(name='ed').first()
    print(our_user)

    session.add_all([
        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
        User(name='mary', fullname='Mary Contrary', nickname='mary'),
        User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

    session.commit()

    print('---- Retrieving all users ----')

    users = session.query(User).all()

    for user in users:
        print(user)
