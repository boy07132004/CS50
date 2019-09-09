import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flight.csv")
    reader = csv.reader(f)
    for ori , dest , dur in reader:
        db.execute('INSERT INTO flights (origin,destination,duration) VALUES \
            (:origin,:destination,:duration)' ,{"origin":ori\
            ,"destination":dest,"duration":dur})
    db.commit()
if __name__ =="__main__":
    main()