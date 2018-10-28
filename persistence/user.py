from sqlalchemy import Column, Integer, String

from persistence.db_core import Base


class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    photo1 = Column(String)
    photo2 = Column(String)
    photo3 = Column(String)
    voted = Column(Integer)
    like = Column(Integer)
    dislike = Column(Integer)
    start_time = Column(String)
    isvoted = Column(String)
    rand = Column(Integer)
    votelist = Column(String)
    votedlist = Column(String)
