#!/usr/bin/python3
"""prints the State object with the name passed as argument """
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost/{sys.argv[3]}")
    with Session(engine) as session:
        result = session.query(State).filter(State.name == sys.argv[4]).first()
        if result:
            print(f"{result.id}")
        else:
            print("Not found")
