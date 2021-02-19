"""In this series of tests, we are looking at time to load a large number
of very small and simple rows.

A special test here illustrates the difference between fetching the
rows from the raw DBAPI and throwing them away, vs. assembling each
row into a completely basic Python object and appending to a list. The
time spent typically more than doubles.  The point is that while
DBAPIs will give you raw rows very fast if they are written in C, the
moment you do anything with those rows, even something trivial,
overhead grows extremely fast in cPython. SQLAlchemy's Core and
lighter-weight ORM options add absolutely minimal overhead, and the
full blown ORM doesn't do terribly either even though mapped objects
provide a huge amount of functionality.

"""
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Bundle
from sqlalchemy.orm import Session


Base = declarative_base()
engine = None


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


def setup_database(num):
    global engine
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    s = Session(engine)
    for chunk in range(0, num, 10000):
        s.execute(
            Customer.__table__.insert(),
            params=[
                {
                    "name": "customer name %d" % i,
                    "description": "customer description %d" % i,
                }
                for i in range(chunk, chunk + 10000)
            ],
        )
    s.commit()

def test_orm_full_objects_chunks(n):
    """Load fully tracked ORM objects a chunk at a time using yield_per()."""

    sess = Session(engine)
    for obj in sess.query(Customer).yield_per(100).limit(n):
        print(obj.name)


if __name__ == "__main__":
    setup_database(1000)
    test_orm_full_objects_chunks(1000)

