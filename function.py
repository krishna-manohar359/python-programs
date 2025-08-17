#print("adding two numbers")
print("Brothers:")
#def display(a,b):
 #   sum=a+b
  #  return sum
#a=display(5,6)
def display(*names):#variablee length arguments
    for i in names:
        print(i)
a=display("soma sundhar","praneeth","kiran","krishna")
#print(a)