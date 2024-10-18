lst = []
length = int(input("Enter the size of the list:"))
print(f"Enter {length} numbers to the list:")
for i in range(length):
    temp = int(input())
    if temp>100:
        lst.append('over')
    else:
        lst.append(temp)
print(f"List:{lst}")
