rock=0
paper=1
scissor=2
import random
choice=int(input("enter a number b/w 0 to 1(0=rock,1=paper,2=scissor)"))
cm_choice=random.randrange(0,3)
print(f"computer choice{cm_choice}\n your choice{choice}")
if choice==cm_choice:
    print("draw")
if choice==1 and cm_choice==2:
    print("congratulation you won the game")
elif choice==2 and cm_choice==0:
    print("congratulation you won the game")
elif choice==1 and cm_choice==0:
   print("congratulation you won the game")
else:
    print("you lose")