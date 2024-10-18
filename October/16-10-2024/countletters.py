lst = []
sum = 0
length = int(input("Enter the length of the list:"))
print(f"Enter {length} first names:")
for i in range(length):
    temp = input()
    lst.append(temp)
for j in lst:
    temp = j.count('a')+j.count('A')
    print(f"{temp} times 'a'/'A' in {j}")
    sum += temp
print(f"Total numer of 'a'/'A' in the list:{sum}")
