class ParkingSystem:

    def __init__(self, big, medium, small):
        # Store available slots in a list: index 1 = big, 2 = medium, 3 = small
        self.slots = [0, big, medium, small]

    def addCar(self, carType):
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False
