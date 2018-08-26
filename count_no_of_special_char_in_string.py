str=[]
count=0
wrds=['~','!','@','#','$','%','^','&','*','(',')','_']
x=input("enter a string")
str=x.split(".")
s=len(str)

for i in range(0,s):
    ch=list(str[i])
    c=len(ch)
    for j in range(0,c):
        if(ch[j] in wrds):
            count+=1
print(count)
