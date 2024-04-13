#!/usr/bin/python3

"""
Module deletes records for states with a
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

    aStates = session.query(State).filter(State.name.like(f"%a%"))
    for aState in aStates:
        session.delete(aState)
    session.commit()
