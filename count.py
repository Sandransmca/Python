s=input(("enter a string:"))
count =0
for i in range (len(s)):
    if s[i]!='':
        count=count+1
print("the total number of characters in the string:",count)
