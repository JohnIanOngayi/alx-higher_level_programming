#!/usr/bin/python3

"""
Module that prints all cities
"""

import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_state_city = session.query(State, City).outerjoin(City).order_by(
        State.id, City.id).all()
    for _state in all_state_city:
        print(f"{_state.id}: {_state.name}")
        for _city in _state.cities:
            print(f"    {_city.id}: {city.name}")
