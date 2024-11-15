def fibonacci(num):
    a = 0
    b = 1
    print("\nFibonacci series:\n")
    print(f"{a}\n{b}")
    for i in range(3,num+1):
        c = a+b
        print(f"{c}")
        a = b
        b = c
