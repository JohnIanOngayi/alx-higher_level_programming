#!/usr/bin/python3

"""
Module that prints all cities
"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    allCities = list(session.query(
        City, State
        ).filter(City.state_id == State.id).order_by(City.id))
    for city in allCities:
        print(f"{city['State'].name}: ({city['City'].id}) {city['City'].name}")
