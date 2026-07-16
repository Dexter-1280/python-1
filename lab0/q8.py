# more pratice question
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and b + c > a and a + c > b:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Area =", area)
else:
    print("Invalid Triangle")
 
 #2
    n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + (2 * i) / i

print("Sum =", sum)
#3
a = float(input("Enter first parallel side: "))
b = float(input("Enter second parallel side: "))
h = float(input("Enter height: "))

area = ((a + b) * h) / 2

print("Area =", area)
#4
pi = 3.14159

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

volume = pi * r * r * h
surfaceArea = 2 * pi * r * (r + h)

print("Volume =", volume)
print("Surface Area =", surfaceArea)
#5 
num = float(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    #6
    a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

#7
    num = input("Enter number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#8
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
#9
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Bill =", bill)
#10
age = int(input("Enter age: "))
test = input("Passed driving test (yes/no): ")

if age >= 18 and test.lower() == "yes":
    print("Eligible")
else:
    print("Not Eligible")