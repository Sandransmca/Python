n=int(input("enter the limit"))
list=[]
sum=0
for i in range(n):
    i=int(input("enter the numbers:"))
    list.append(i)
print(list)
for i in list:
    sum=sum+i
print("sum of list:",sum)
