s=input("Enter a string: ")
vowels=("A","a","E","e","I","i","O","o","U","u")
num=0
for i in s:
    if i in vowels:
        num=num+1
        print(i)
print("No. of vowels in this string is = ",num)

