#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost/{sys.argv[3]}")
    Session = sessionmaker(engine)
    session = Session()
    result = session.execute(select(State).where(State.id == 1))
    for state in result.scalars():
        print(f"{state.id}: {state.name}")
    session.close()
