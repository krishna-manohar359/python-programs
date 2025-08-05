row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
l=[[1,1,1],[1,1,1],[1,1,1]]
print(f"{row1}\n{row2}\n{row3}")
a=input("enter position wher you want to put money:")
print(a)
row_number=int(a[0])
column=int(a[1])
l[row_number-1][column-1]='x'
print(f"{row1}\n{row2}\n{row3}")
