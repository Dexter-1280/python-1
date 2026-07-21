s = "Python Programming"

print(s.lower())
print(s.title())
print(s.swapcase())
print(s.startswith("Python"))
print(s.endswith("ing"))
print(s.find("Pro"))
print(s.count("m"))

text = "Ramdeobaba University"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)



marks = [78, 92, 65, 88, 95]

print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks))

marks.sort()
print(marks)