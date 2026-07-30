number = [8,9,9,1,6,9,5,7,3,9,7,3,4,8,3,5,8,4,8,7,5,7,3,6,1,2,7,4,7,7,8,4,3,4,2,2,2,7,3,5,6,1,1,3,2,1,1,7,7,1,4,4,5,6,1,2,7,4,5,8,1,4,8,6,2,4,3,7,3,6,2,3,3,3,2,4,6,8,9,3,9,3,1,8,6,6,3,3,9,4,6,4,9,6,7,1,2,8,7,8,1,4]

price = [195,225,150,150,90,60,75,255,270,225,135,195,30,15,210,105,15,30,180,60,165,60,45,225,180,90,30,210,150,15,270,60,210,180,60,225,150,150,120,195,75,240,60,45,30,180,240,285,135,165,180,240,60,105,165,240,120,45,120,165,285,225,90,105,225,45,45,75,180,90,240,30,30,60,135,180,15,255,180,270,135,105,135,210,180,135,195,225,75,225,15,240,60,15,180,255,90,15,150,230,150]

print("a) Different products =", len(set(number)))

print("b) Total items sold =", len(number))

avg = sum(price) / len(price)
print("c) Average price =", avg)

print("d) Costliest item =", max(price))

revenue = 0
for i in range(len(number)):
    revenue += number[i] * price[i]
print("e) Total revenue =", revenue)

print("f)", number[19] > number[49])

count = 0
for p in price:
    if p > avg:
        count += 1
print("g) Expensive products =", count)

students = (
    (1, "Amit", "Nagpur", 85, 90, 88),
    (2, "Riya", "Pune", 92, 95, 91),
    (3, "Rahul", "Mumbai", 70, 75, 80),
    (4, "Sneha", "Delhi", 89, 91, 87),
    (5, "Karan", "Nashik", 78, 82, 80),
    (6, "Priya", "Bhopal", 95, 94, 96),
    (7, "Neha", "Indore", 88, 85, 90),
    (8, "Arjun", "Hyderabad", 81, 79, 84),
    (9, "Rohan", "Jaipur", 73, 77, 75),
    (10, "Anjali", "Chennai", 90, 89, 92)
)

students = sorted(students, key=lambda x: x[0])

total = []
for s in students:
    marks = s[3] + s[4] + s[5]
    total.append((marks, s))

total.sort(reverse=True)

print("Top 3 Students")
for i in range(3):
    print(total[i][1])



s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = set(s1) & set(s2)

print("Common letters are:")
for ch in common:
    print(ch, end=" ")



L = [1, 2, 3, 4, 5]

k = int(input("Enter number of rotations: "))

k = k % len(L)

L = L[k:] + L[:k]

print("Rotated List:", L)