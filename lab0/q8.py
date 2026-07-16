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
    n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + (2 * i) / i

print("Sum =", sum)

a = float(input("Enter first parallel side: "))
b = float(input("Enter second parallel side: "))
h = float(input("Enter height: "))

area = ((a + b) * h) / 2

print("Area =", area)