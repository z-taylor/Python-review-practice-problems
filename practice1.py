def findAverage(list):
    var = 0
    for i in range(len(list)):
        var = var + list[i]
    var = var/len(list)
    return var

flag = True
list = []
while flag:
    num = int(input("Type a number, or -1 to quit: "))
    if num==-1:
        flag = False
        print(f"The average of all the numbers you entered is: {findAverage(list)}")
    else:
        list.append(num)