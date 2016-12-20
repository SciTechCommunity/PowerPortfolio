# /models/project.py
from sqlalchemy import (
        Column,
        Integer,
        String,
        Boolean 
)
from .base import Base

class Project(Base):
    """
    Describes a project that has been contributed to or performed by the admin.
    Contains information such as a link to the project, and a description of
    the project and the admin's part in it.
    """
    __tablename__ = "projects"

    key = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    show = Column(Boolean)
    description = Column(String)

    def to_json(self):
        """ Converts the project to json """
        return dict(
            key=self.key,
            name=self.name,
            url=self.url,
            show=self.show,
            description=self.description
        )
