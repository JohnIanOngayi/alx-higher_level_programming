#!/usr/bin/python3

"""
Module queries db to obtain states
"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    allStates = list(session.query(State).order_by(State.id))
    for _ in range(0, len(allStates)):
        print("{0}: {1}".format((_ + 1), allStates[_].name))
