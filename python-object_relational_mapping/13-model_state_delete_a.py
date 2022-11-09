#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost/{sys.argv[3]}")
    with Session(engine) as session:
        session.query(State).filter(State.name.like('%a%')).\
                delete(synchronize_session='fetch')
        session.commit()
