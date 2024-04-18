#!/usr/bin/python3

"""
Module defines class states
"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    Class inherits from SQL class Base
    it is used to define table for states
    """
    __tablename__ = "states"
    id = Column(
            "id",
            Integer,
            autoincrement=True,
            primary_key=True,
            unique=True,
            nullable=False
            )
    name = Column(
        "name",
        String(length=128),
        nullable=False
    )

    cities = relationship('City', backref='state', cascade='all, delete')
