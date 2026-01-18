class Airport():
    def __init__(self, passengers = {}, gates = []): #Defines initial function to set the essential properties of Airport class.
        self.passengers = passengers #Passengers are kept as dictionaries to sort them by class. Check the airport object (line 33) below.
        self.gates = gates

    def add_passenger(self, passenger = ("", "Economy")): #Adds it to the list of passengers
        self.passengers[passenger[1]].append(passenger[0])

    def assign_after_all_added(self):
        for i in self.passengers: #Loops through the passenger classes.
            for j in self.passengers[i]: #Loops through the passengers within the classes.
                added = False
                for h in self.gates:
                    if (not added) and (len(h.passengers) < h.capacity): #Checks if the passenger has been added before and if the gate has capacity.
                        added = True
                        h.passengers.append((j, i))
                        break #Skips to the next passenger once it adds a passenger to a gate.
                if not added:
                    print(f"Dropped due to priority/capacity: {j} ({i})")

    def print_gates(self):
        for i in self.gates:
            print(i.name + ":", i.passengers)

class Gate():
    def __init__(self, name, capacity, passengers = []):
        self.name = name
        self.capacity = capacity
        self.passengers = passengers

Gate1 = Gate("Gate 1", 3, []) #Editor Note: Not adding the [] whilst solving the lab has caused me to score 0 that week.
Gate2 = Gate("Gate 2", 2, []) #Another reason that I hate how different lists can be directed to the same memory address.
airport = Airport({"VIP":[], "Business":[], "Economy":[]}, [Gate1, Gate2])

airport.add_passenger(("Alice", "Economy"))
airport.add_passenger(("Bob", "VIP"))
airport.add_passenger(("Charlie", "Business"))
airport.add_passenger(("Diana", "VIP"))
airport.add_passenger(("Ethan", "Economy"))
airport.add_passenger(("Frank", "Business"))
airport.add_passenger(("Gina", "VIP"))
airport.assign_after_all_added()
airport.print_gates()