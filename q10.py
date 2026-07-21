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