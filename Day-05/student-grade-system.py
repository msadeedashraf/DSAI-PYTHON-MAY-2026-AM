student_name = input("Enter student name: ")
student_mark = float(input("Enter the student mark: "))

if   student_mark >= 90:
        grade = "A+"
elif student_mark >= 80:
        grade = "A"
elif student_mark >= 70:
        grade = "B"
elif student_mark >= 60:
        grade = "C"
elif student_mark >= 50:
        grade = "D"
else:
        grade = "F"

print("================================")
print("Student Grade Report")
print("================================")
print("Student:", student_name)
print("Mark:", student_mark)
print("Grade:", grade)  
