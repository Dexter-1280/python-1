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
    