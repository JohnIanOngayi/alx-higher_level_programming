#!/usr/bin/python3

"""
Module defines db table to store cities
"""

from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
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
