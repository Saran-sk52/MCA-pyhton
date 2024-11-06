def fibonacci(r):
    lst = []
    for i in range(r):
        if i==0 or i==1:
            lst.append(i)
        else:
            number=lst[i-1]+lst[i-2]
            lst.append(number)
    print(lst)
r = int(input("Enter the range:"))
fibonacci(r)
