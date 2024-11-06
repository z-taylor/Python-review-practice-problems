names = []
for i in range(5):
    i+=1
    names.append(input(f"Input name {i}: "))
names.sort()
print(names[4])