"this is multiple line  comment "
# this is single line comment

#taking input
x=int(input("Enter your age:"))
print("your age is",x)
gender=str(input("Male or female:"))
print("Enter your gender")
if(x<18):
    print("This is not legal age to drive")
    if(gender!="female"):
        print("you need to be 21 year old to drive.")
    else:
        print("Cong!!!!")

else:
    print("You have legal age to drive")    

    #spacing is important in python
    