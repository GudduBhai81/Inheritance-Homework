class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 500 


class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (0.1 * base_fare)
        return total_fare


bus = Bus("School Bus", 50)
print(f"Total fare for {bus.name} with capacity {bus.capacity}: {bus.fare()} PKR")