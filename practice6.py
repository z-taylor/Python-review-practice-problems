def timesTable(num):
    for i in range(13):
        print(f"{num} x {i} = {num*i}")
timesTable(float(input("Enter a number to get a times table for: ")))