n=int(input("enter the limit:"))
list=[]
for i in range(n):
    i=input("enter the word:")
    list.append(i)
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>max):
        max=len(i)
        temp=i
print("the word having longest length",temp,"and its length is:",max)