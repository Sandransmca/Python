n=int(input("Enter the number of word:"))
list=[]
for i in range(n):
    x=input("Enter the word:")
    list.append(x)
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if (len(i)>max):
        max=len(i)
        temp=i
print("The word having longest lenth is:",temp,"and its lenth is:",max)