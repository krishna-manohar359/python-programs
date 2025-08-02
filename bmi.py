weight=input("enter weight")
height=input ("enter height")
bmi=int(weight)/float(height) ** 2
print(bmi)
if bmi<18.5:
    print("undr weight")
elif bmi<=25:
    print("normal weight")
elif bmi<=30:
    print("hevay weight")
else :
  print("obese")