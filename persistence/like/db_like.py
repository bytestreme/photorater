from persistence.user import User
from sqlalchemy.orm import relationship, backref, sessionmaker
from persistence.db_core import engine, Base


# SET (init) of like to user(id)
def db_like_set(id, init):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    s.query(User).filter(User.uid == id).update({'like': init})
    s.commit()


def db_dislike_set(id, init):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    s.query(User).filter(User.uid == id).update({'dislike': init})
    s.commit()


def db_dislike_get(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first()
    result = user.dislike
    s.commit()
    return int(result)


# GET number of like  of user(id)
def db_like_get(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first()
    result = user.like
    s.commit()
    return int(result)
