a=[]
x=input("enter something")
a=x.split(' ')
sum=0
for i in range(0,len(a)):
    l=len(a[i])
    sum=sum+l
print(sum)
