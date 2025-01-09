n=int(input("enter the limit"))
first=0
second=1
print(first)
print(second)
for i in range(n-2):
    third=first+second
    first=second
    second=third
    print(third)
