#!/usr/bin/python3

"""
Module queries db to obtain states with 'a' in name
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

    allStates = list(session.query(State).filter(State.name.like(f"%a%"))
                     .order_by(State.id))
    for state in allStates:
        print(f"{state.id}: {state.name}")
