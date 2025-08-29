#command line in python and executing in cmd 
import sys
#print(sys.argv)
#(len(sys.argv))
sum=0
#for i in range(0,len(sys.argv)):
#    print("argument-",i,":",sys.argv[i])
for i in range(1,len(sys.argv)):
    sum+=int(sys.argv[i])
    print("result=",sum)
