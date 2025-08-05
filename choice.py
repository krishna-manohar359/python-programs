import random
name=input("enter names of member :")
print(name)
l=name.split(",")
print(l)
length=len(l)
name_1=random.randrange(0,length-1)
print(f"{l[name_1]} is going to pay the bill")
