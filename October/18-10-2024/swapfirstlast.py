strr = input("Enter a string:")
print(f"String before swapping:{strr}")
if len(strr)>1:
    strr2 = strr[-1]+strr[1:-1]+strr[0]
else:
    strr2 = strr1
print(f"String after swapping:{strr2}")
