def listMulti(list):
    numbers = []
    for i in range(int(len(list)/2)):
        num = list[i] + list[-(i+1)]
        numbers.append(num)
    return numbers

flag = True
numbers = []
run = 0
while flag:
    run+=1
    num = int(input("Enter a number: "))
    if run>=6 and run%2==0:
        flag = True if input("Continue entering numbers? Y/N: ").lower()=="y" else False
    numbers.append(num)

print(listMulti(numbers))