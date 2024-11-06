def testReverse(string1, string2):
    string3 = ""
    for i in range(len(string1)):
        string3 = string3 + string1[-(i+1)]
    if string2 == string3:
        return True
    else:
        return False

string1 = str(input("enter a string: "))
string2 = str(input("enter a string: "))
if testReverse(string1, string2):
    print("your second string is a reverse of the first")
else:
    print("your second string is not a reverse of the first")