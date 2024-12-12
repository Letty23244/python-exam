# i
Age = int(input("Enter your Age"))
if Age>=18:
    print("Your are eligible")
else:
    print("Your are not eligible")
#(ii)
def grade_student():
    student_mark =int(input("enter the marks scored "))
    if student_mark>= 90:
        print("A")
    elif student_mark<=89 and student_mark>80:
        print("B")
    elif student_mark>=79 and student_mark>70:
        print("C")
    elif student_mark>=69 and student_mark>60:
        print("D")
    else:
        print('F')
mark =85
print(mark)
grade_student()
#(iii)
def grade_student(marks):
     marks = int(input("Enter the marks please:"))
     if marks >=90:
        print('Thats grade A' )
     elif marks >=80 and marks < 89:
         print("Thats grade B")
     elif marks >=70 and marks < 79:
         print("Thats grade C")
     elif marks >= 60 and marks< 69:
         print('The grade is D' )
     elif marks < 60:
         print('The Grade is F')
     else:
         return "Invalid Input"
grade_student(mark)
     
#(v)
def grade_student(marks):
     marks = int(input("Enter the marks please:"))
     if marks >=90:
        print('Thats grade A' )
        print('Excellent')
     elif marks >=80 and marks < 89:
         print("Thats grade B")
         print('Excellent')
     elif marks >=70 and marks < 79:
         print("Thats grade C" )
         print('Good')
     elif marks >= 60 and marks< 69:
         print('The grade is D' )
         print('Satisfactory')
     else:
         print('The Grade is F')
         print('Needs Improvement')
mark = 75
grade_student(mark)


