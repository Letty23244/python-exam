# (i)
def circle_area():
    import math
    pi = 3.14
    radius = int(input("enter the radius of the circle"))
    area = pi*(radius**2)
    radius = 4
    print(f" the  area of circle with {radius} is {area}")
circle_area()

#(ii)
def sumOfOddNumbers():
    numbers = [4,7,2,9,12,15]
    print(numbers)
    for num in numbers:
        print(num)
sumOfOddNumbers()
    

    
#(iii)
def twoNumbers(num1,num2):
    number = int((num1,num2))
    return number
num1 =float(input("enter the first number:"))
num2 = float(input("enter second number:"))
sum=0
sum = (num1+num2)
print(f"the sum of two numbers is:{sum}")

difference =0
difference =(num1-num2)
print(f"the difference of two numbers is:{difference}")

product =0
product =(num1*num2)
print(f"the product of the two numbers is:{product}")

quotient =0
quotient =(num1//num2)
print(f"the quotient of the two numbers is:{quotient}")
    

#(v)
def student_info():
    student_info ={'name':'Alice','age':20, 'grade':'A'}
    print(student_info)
    student_info['age'] =26
    print(student_info)
    student_info['city'] = 'Kampala'
    print(student_info)
student_info()

