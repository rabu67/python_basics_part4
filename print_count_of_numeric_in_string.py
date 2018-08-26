str=[]
count=0
x=input("enter a string")
str=x.split(".")
s=len(str)

for i in range(0,s):
    ch=list(str[i])
    c=len(ch)
    for j in range(0,c):
        if(ch[j].isnumeric()):
            count+=1
print(count)
