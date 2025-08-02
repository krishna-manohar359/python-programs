y=input(" enter your name:")
h=input("enter (he/her) name:")
combining=y+h
l_c=combining.lower()
t=l_c.count('t')
r=l_c.count('r')
u=l_c.count('u')
r=l_c.count('r')
e=l_c.count('e')
true=t+r+u+e
l=l_c.count('l')
o=l_c.count('o')
v=l_c.count('v')
e=l_c.count('e')
l=l+o+v+e
love=int(str(true)+str(l))
if love <= 25:
    print(f"your love score={love} \n loveis bad")
    if love > 25 and love <=50:
       print(f"your love score={love} \n love is average")
elif love > 50 and love<=80:
    print(f"love score is{love}\n is good")
else:
     print(f"love score is{love}\n is very good")