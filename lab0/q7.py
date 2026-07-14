#(A)Write a python program to calculate Euclidean distance between two points A(x1,y
#B(x2,y2). Try accepting values as input from user


import math
x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("D:",d)



#(B)Write a python code for calculating the depreciation of car value. Note: For the
#car losses 20 % value, next 4 year loss is 10% per year, after 5 years losses 5% pe
#Input is: original price and car age, output is: current value



carAge = int(input("Enter the car age: "))
currentValue = int(input("Enter current value: "))

if carAge == 1:
    originalPrice = 0.2 * currentValue
elif carAge > 1 and carAge < 5:
    originalPrice = 0.1 * currentValue
else:
    originalPrice = 0.05 * currentValue

print("Final price is", originalPrice)


#(C) Write a python program to generate employee salary slip. Accept from user: name
#employee, basic salary, HRA%, DA%, Tax%.



name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
hra_percent = float(input("Enter HRA %: "))
da_percent = float(input("Enter DA %: "))
tax_percent = float(input("Enter Tax %: "))
performance_bonus = float(input("Enter Performance Bonus: "))

hra=(hra_percent /100)*basic_salary
da=(da_percent/100)*basic_salary
gross_salary=basic_salary+hra+da
tax=(tax_percent/100)*gross_salary
net_salary=gross_salary-tax
final_salary=net_salary+performance_bonus


print("********SALARY SLIP******")
print("Name-",name)
print("*************************")
print("HRA-",hra_percent)
print("DA-",da_percent)
print("TAX-",tax)
print("*************************")
print("Net-salary-",net_salary)
print("*************************")
print("Performance bouns(+0.02)=",performance_bonus)
print("Final salary-",final_salary)

#(D) Write a Python program to find the sum of the series:

n=int(input("Enter the number of terms (n): "))
s=0
for i in range(1, n + 1):
     s =+1/(i*(i + 1))
print(f"The sum of the series up to {n} terms is:{s:.4f}")