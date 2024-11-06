date = input("Input a date in the format of MM/DD without a leading 0: ")
month, day = date.split("/")
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
match day:
    case day if day[-1]=="1" and int(day)!=11:
        suffix = "st"
    case day if day[-1]=="2" and int(day)!=12:
        suffix = "nd"
    case day if day[-1]=="3" and int(day)!=13:
        suffix = "rd"
    case _:
        suffix = "th"
print(f"{day}{suffix} day of {months[int(month)]}")