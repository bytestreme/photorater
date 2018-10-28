from sqlalchemy.orm import relationship, backref, sessionmaker
from persistence.db_core import engine, Base
from persistence.user import User
from random import randint


# GET (i)-th photo_id of (id) user
def db_ph_get(id, i):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    result = "None"
    if i == 1:
        result = s.query(User).filter(User.uid == str(id)).first().photo1
    elif i == 2:
        result = s.query(User).filter(User.uid == id).first().photo2
    elif i == 3:
        result = s.query(User).filter(User.uid == id).first().photo3

    s.commit()
    return result


# SET string(st) as (i)-th photo_id of user with (id)
def db_ph_set(id, i, st):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    field = 'photo' + str(i)
    s.query(User).filter(User.uid == id).update({field: st})
    s.commit()


# Check if user is in db, if NOT: Create new record with default "empty" values
def store(id, username, first_name, last_name):
    result = False

    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user_exists = s.query(User).filter(User.uid == id).first()
    if user_exists is None:
        new_user = User(uid=id, username=username, first_name=first_name, last_name=last_name, photo1='None',
                        photo2='None', photo3='None', voted=99, like=0, dislike=0, start_time=func.now(),
                        isvoted='False', rand=randint(1, 3), votedlist=None, votelist=None)
        print('Creating new user with uid:' + str(id))
        s.add(new_user)
    else:
        print('Existing user with uid:' + str(id))
        result = True
    s.commit()
    return result


# GET value of field filtering by id
def db_value_get(id, field):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first()
    result = getattr(user, field, None)
    s.commit()
    return result


# SET value into field filtering by id
def db_value_set(id, field, value):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    s.query(User).filter(User.uid == id).update({field: value})
    s.commit()


# GET from db number randomly set for each user(id) on registration
def db_rand_get(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first()
    result = user.rand
    s.commit()
    return result


# Returns random id of other user
def get_rand_id(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first()
    result = user.votelist
    result = result.split('\n')
    s.commit()
    return result[randint(0, len(result) - 1)]


# Find intersection of two Lists
def intersection(lst1, lst2):
    try:
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3
    except TypeError:
        return []


