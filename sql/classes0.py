class Flight :
    counter = 1
    def __init__(self,origin,destination,duration):
        self.id = Flight.counter
        Flight.counter +=1
        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration
    def print_info(self):
        print(f"Flight origin:{self.origin}")
        print(f"Flight destination:{self.destination}")
        print(f"Flight duration:{self.duration}")
        print(f"\nPassenger:")
        if len(self.passengers) == 0:print("No passenger")
        else:
            for passenger in self.passengers:
                print(f"{passenger.name}")
    def delay(self,amount):
        self.duration+=amount
    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:
    def __init__(self,name):
        self.name = name

def main():
    f1 = Flight("New York","Paris",540)
    f1.print_info()
    print("-----------")
    ZM = Passenger("Zheming")
    f1.add_passenger(ZM)
    f1.print_info()
    print("-----------")

    """     test f2
    f2 = Flight("Tokyo","Shanghai",185)
    f2.print_info()
    """
    """     test delay
    f1.delay(20)
    f1.print_info()
    """
if __name__ == "__main__":
    main()