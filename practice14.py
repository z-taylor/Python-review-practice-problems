string = "cse1321:3:A,cse1321L:1:B,ENGL1101:3:B,MATH1190:4:C"
list = string.split(",")
numHours, gpaCalc = 0, 0
for course in list:
    className, hours, letterGrade = course.split(":")
    print(f"Course: {className}     Hours: {hours}     Letter grade: {letterGrade}")
    if letterGrade=="A":
        numberGrade = 4
    elif letterGrade=="B":
        numberGrade = 3
    elif letterGrade=="C":
        numberGrade = 2
    elif letterGrade=="D":
        numberGrade = 1
    else:
        numberGrade = 0
    numHours += int(hours)
    gpaCalc += int(hours)*numberGrade
gpa = gpaCalc/numHours
print(f"Final gpa: {gpa}")