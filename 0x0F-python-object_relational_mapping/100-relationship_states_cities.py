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

    california = State(name='California')
    san_francisco = City(name='San Francisco', state='California')
    session.add_all([california, san_francisco])
    session.commit()
    session.close()
