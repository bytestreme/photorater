from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import config

Base = declarative_base()
engine = create_engine(config.engine_uri)
