#types of exception handling
a=int(input("enter value of a:"))
b=int(input("enter a value of b:"))
#if exception occured then output is not printed
try:
    c=a/b
    print(c)
except: 
    print("exception occured:")
else:
    print("excception not raised")
finally:
    print("programme ends....")