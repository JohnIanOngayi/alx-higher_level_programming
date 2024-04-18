#!/usr/bin/python3

"""
Module defines db table to store cities
"""

from sqlalchemy import String, Integer, Column, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    Mapped class to store cities
    """
    __tablename__ = "cities"
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
    state_id = Column(
            "state_id",
            Integer,
            ForeignKey("states.id"),
            nullable=False
            )
