def fib(n) : 
    global count_fib
    if n == 1 or n == 2 :
        count_fib += 1
        return 1
    else :
        return (fib(n - 1) + fib(n - 2))

n = int(input())
f = [0] * (n+1)
count_fib = 0

fib(n)
print(count_fib, n-2)