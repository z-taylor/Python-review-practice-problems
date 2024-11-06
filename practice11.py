def checkPassenger(passengers, check):
    for row in passengers:
        for passenger in row:
            if passenger==check:
                return True
    return False
passengers=[['Alice', 'Bob'], ['Charlie', 'David'], ['Eva', 'Frank'], ['Grace', 'Hannah'], ['Ian', 'Jack'], ['Kathy', 'Leo'], ['Mia', 'Nina'], ['Oscar', 'Paul']]
passengerCheck = input("Enter the name of the passenger you want to find: ")
if checkPassenger(passengers, passengerCheck):
    print(f"{passengerCheck} is on the passenger list.")
else:
    print(f"{passengerCheck} is not on the passenger list.")