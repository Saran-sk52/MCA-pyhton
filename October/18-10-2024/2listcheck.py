lst1 = []
len1 = int(input("Enter the size of first list:"))
print(f"Enter {len1} numbers to the first list:")
for i in range(len1):
    temp = int(input())
    lst1.append(temp)

lst2 = []
len2 = int(input("Enter the size of second list:"))
print(f"Enter {len2} numbers to the second list:")
for j in range(len2):
    temp = int(input())
    lst2.append(temp)

if len1 == len2:
    print("Both lists are of same length")
else:
    print("Both lists are of different length")

if sum(lst1) == sum(lst2):
    print("Sum of both lists are same")
else:
    print("Sum of both lists are different")

for i in lst1:
    if i in lst2:
        print(f"'{i}' occurs in both lists")
