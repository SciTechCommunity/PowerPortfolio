# /models/__init__.py
from .project import Project
from .base import Base
from portfolio.application import application

from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(application.config["DATABASE"], echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
)

def needs_db(function):
    """ A function wrapper that provides access to the database. """
    @wraps(function)
    def wrapper(*args, **kwargs):
        db_session = Session()
        output = function(db_session, *args, **kwargs)
        db_session.close()
        return output
    return wrapper
