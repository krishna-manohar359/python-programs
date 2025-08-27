#creating a file
f=open("student details.txt","w")# used to open file and compiler assumes that it is opend to wirte the data
f.write("name:krishna\nroll no: 174\n age:17")
f=open("student details.txt","r")# file is opend for reading purpose
print(f.read())
f.seek(0)#moves pointer to first again
print(f.readline())
f1=open("krishna.txt","w")
f1.write("hello programmer welcome to programing ")
line=["harsha vardhan ","jein ","karthik "]
f1.writelines(line)# write and read only list
f1.close()
f1=open("krishna.txt","r")
print(f1.readlines())# read every line and only list
f1.close()
f1=open("krishna.txt","a")#append it adds the text at the end of file
f1.write("\nhello") 
f.close()
f1=open("krishna.txt","r")
print(f1.read())
f1.close()