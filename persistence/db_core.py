from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine
import config

Base = declarative_base()
engine = create_engine(config.engine_uri)


