n1=int(input("Enter the 1st number"))
n2=int(input("Enter the 2nd number"))
n3=int(input("Enter the 3rd number"))
if n1>n2 and n1>n3:
    print(f"The largest number is {n1}")
elif n2>n1 and n2>n3:
    print(f"The largest number is {n2}")
else:
    print(f"The largest number is {n3}")
    
