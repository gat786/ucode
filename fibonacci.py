def fibonacci(n):
    a=1
    b=1
    print("Fibonacci series starts ")
    print(a)
    print(b)
    fibo=a+b
    print(fibo)
    while (fibo<n):
        a=b
        b=fibo
        fibo=a+b
        if fibo<n:
            print(fibo)
a=int(input("Enter a number till you want fibnacci series"))
fibonacci(a)