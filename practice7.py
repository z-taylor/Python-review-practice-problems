priceList = []
numPeople = int(input("How many people are going to the movie theater? "))
for i in range(numPeople):
    i+=1
    match i:
        case i if i<=20:
            priceList.append("$10")
        case i if 20<i<=40:
            priceList.append("$12")
        case i if 40<i<=60:
            priceList.append("$13")
        case i if 60<i<=80:
            priceList.append("$16")
        case i if i>80:
            priceList.append("$20")
print(priceList)