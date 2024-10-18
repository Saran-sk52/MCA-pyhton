lst=[1,2,3,4,5,6,7,8,9]
print(f"The list is {lst}")
length =len(lst)
temp=lst[0]
lst[0]=lst[length-1]
lst[length-1]=temp
print(f"The swapped list is {lst}")
