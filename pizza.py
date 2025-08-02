piza=input("enter the pizza size you want small,medium and large:")
bill=0
if piza=="small":
   bill +=100
   print("price of piza is 100")
elif piza=="medium":
     bill +=200
     print("price of medium piza is 200")
else :
    bill +=300
    print("large pizza price is 300")
p=input("you want peporonie (Y/N) enter:")
if p == 'y'or p=='Y':
    if piza == "small":
        bill += 30
        print("price 30")
    elif piza == "medium":
        bill += 40
        print("price 40" )
    else: 
        bill += 50
        print("price 50" )
cheez=input("you want cheez (y/n):")
if cheez=='Y'or cheez=='Y':
    bill += 20
print(f"final bill{bill}:")