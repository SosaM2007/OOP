Stu_name=input("Enter the student Name:")
course1 = int(input("Enter the grade points for course1:"))
course2 = int(input("Enter the grade points for course2:"))
course3 = int(input("Enter the grade point for course3:"))
course4 = int(input("Enter the grade points for course4:"))
course5 = int(input("Enter the grade points for course5:"))

total = course1+course2+course3+course4+course5
print ("The total grade points is: 480:")
average = total / 5
print("the average is",average)

if average <100 and average >90:
    print("Grade A")
elif average <89 and average >79:
    print("Grade B")
elif average <79 and total_percentage >69:
    print("Grade C")
elif average <59 and average >70:
    print("Grade D")
else:
    print("Grade F")


