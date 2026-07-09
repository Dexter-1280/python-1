"Task:2 from hackerrank"
#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

a=int(input("Enter your first num a:"))
b=int(input("Enter your first num b:"))

sum=a+b
print("The sum of two number is",sum)
difference=a-b
print("The difference of first and second number",difference)
product=a*b
print("The product of a and b is",product)

"Task 3 of hackerrank"
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

#No rounding or formatting is
div1=a//b
print("Result is without decimal point",div1)
div2=a/b
print("Result wiht decimal point",div2)

"Task 4 of hackerrank"
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n , print i^2.

n=int(input("Enter the num n:"))


for i in range(n): #for i in range(start,stop,step):
    i =i ** 2
    print(i,"\n")

"Task 5 of hackerrank"
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

#In the Gregorian calendar, three conditions are used to identify leap years:

#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

year=int(input("Enter the year to determine:"))
def is_leap(year):
     print("False")
def isnot_leap(year):
      print("True")

if year % 400 == 0:
    is_leap(year)
elif year % 100 == 0:
    isnot_leap(year)
elif year % 4 == 0:
    is_leap(year)
else:
    isnot_leap(year)

"Task 3 from lab "
#Electricity Bill Calculation
#Write a Python program to calculate the electricity bill based on the following tariff:

#First 100 units: ₹2 per unit
#Next 200 units: ₹3 per unit
#Remaining units: ₹5 per unit"
def electricity_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 200 * 3 + (units - 300) * 5

    return round(bill, 2)

units = int(input("Enter electricity units consumed: "))
print("Electricity Bill: ₹", electricity_bill(units))    


"Task 4 from lab"
#using some math property by importing math
#Program to find the roots of a quadratic equation entered by the user.
import math


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", root1, root2)

elif d == 0:
    root = -b / (2*a)
    print("Both roots are:", root)

else:
    print("No real roots")

"Task 6 of hackerrank"
#The included code stub will read an integer,n, from STDIN. Without using any string methods, try to print the following
x1w = int(input())
for i in range(x1w):
    print(i)