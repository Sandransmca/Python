s=input("enter a string:")
if s.endswith("ing"):
    s=s+"ly"
else:
    s=s+"ing"
print("modified string is:",s)