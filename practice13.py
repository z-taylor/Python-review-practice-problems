class elevator:
    def __init__(self, elevatorNumber, currentFloor = 1, destinationFloor = 1, weight = 0):
        self.elevatorNumber = elevatorNumber
        self.currentFloor = currentFloor
        self.destinationFloor = destinationFloor
        self.weight = weight
    def move(self, targetFloor):
        self.destinationFloor = targetFloor
        print(f"Elevator number {self.elevatorNumber} moving from floor {self.currentFloor} to floor {self.destinationFloor}")
        for i in range(self.currentFloor, self.destinationFloor+1):
            print(f"Now on floor {i}")
        print(f"Elevator number {self.elevatorNumber} arrived at floor {self.destinationFloor}")

elevator1 = elevator(1)
elevator2 = elevator(2)
elevator1.move(5)
elevator2.move(10)