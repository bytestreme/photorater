from random import shuffle

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from persistence.db_actions import intersection, db_value_get
from persistence.db_core import engine, Base
from persistence.user import User


# GET voteDlist of user(id)
def db_votedlist_get(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first().votedlist
    if user is None:
        result = None
    else:
        result = user.split('\n')
    s.commit()
    return result


# ADD (st) to 'voteDlist' of user(id)
def db_votedlist_add(id, id2):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    pre = ''.join(db_votedlist_get(id)) + '\n' + str(id2)
    s.query(User).filter(User.uid == id).update({'votedlist': pre})
    s.commit()


# SET (init) of vote points to user(id)
def db_vote_set(id, init):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    s.query(User).filter(User.uid == id).update({'voted': init})
    s.commit()


# GET number of vote points of user(id)
def db_vote_get(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first()
    result = user.voted
    s.commit()
    return result


def db_vote_not_voted_get(id):
    alr = db_votedlist_get(id)
    stnt = db_votelist_get(id)
    if len(alr) == len(stnt):
        return None
    else:
        inrt = intersection(alr, stnt)
        for x in inrt:
            stnt.remove(x)
        return stnt[0]


def db_votelist_gen(id):
    newlist = ""
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    users = s.query(User).filter(
        and_(User.uid != id, User.photo1 != 'None', User.photo2 != 'None', User.photo3 != 'None')).all()
    for x in users:
        newlist += str(x.uid) + '\n'
    newlistsh = newlist.split('\n')
    shuffle(newlistsh)
    newlistsh.remove("")
    toadd = '\n'.join(newlistsh)
    s.query(User).filter(User.uid == id).update({"votelist": toadd})
    s.commit()


# Update 'votelist' for user(id)
def db_votelist_update(id):
    check = db_value_get(id, "votelist")
    if check is None:  # in case of empty votelist field
        db_votelist_gen(id)  # generate new votelist
    else:  # if votelist exists
        check = check.split('\n')  # pre existing votelist turn to array
        try:
            check.remove("")  # removed last lane with "\n"
        except ValueError:
            pass
        vlsize = len(check)  # number of users in pre existing votelist
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        newlist = ""
        newusers = s.query(User).filter(and_(User.uid != id, User.photo1 != 'None', User.photo2 != 'None',
                                             User.photo3 != 'None')).all()  # get all uid except self
        for x in newusers:
            newlist += str(x.uid) + '\n'  # write to string separated with newline
        newlist = newlist.split('\n')  # turn to array
        newlist.remove("")
        inrs = intersection(newlist, check)
        if len(newlist) != vlsize:
            for o in inrs:
                newlist.remove(o)
            shuffle(newlist)
            result = check + newlist
            toadd = '\n'.join(result)
            s.query(User).filter(User.uid == id).update({"votelist": toadd})
        s.commit()


def db_votelist_get(id):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    user = s.query(User).filter(User.uid == id).first().votelist
    result = user.split('\n')
    s.commit()
    return result
