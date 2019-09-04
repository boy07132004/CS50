import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT id,origin,destination,duration FROM flights ORDER BY id").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}")
    flight_id = int(input("\nFlight ID:"))
    flight = db.execute("SELECT origin ,destination, duration FROM flights WHERE id = :id"\
        ,{"id":flight_id}).fetchone()
    if flight is None:
        print ("ERROR : No such flight.")
        return
    passengers = db.execute("SELECT name From passengers WHERE flight_id = :id",\
        {"id" : flight_id}).fetchall()
    if len(passengers)==0:
        print("No passengers.")
    else:
        for passenger in passengers:
            print(passenger.name) 
if __name__ =="__main__":
    main()