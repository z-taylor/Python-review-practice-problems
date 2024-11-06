def testPal(string1):
    string2 = string1[::-1]
    if string1 == string2:
        return True
    else:
        return False
    
string1 = str(input("enter a string: "))

if testPal(string1):
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")