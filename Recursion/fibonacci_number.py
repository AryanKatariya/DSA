def fibonacci_no(n):
    if n == 1 or n == 2:
        return 1
    fib_n_1 = fibonacci_no(n-1)
    fib_n_2 = fibonacci_no(n-2)
    output = fib_n_1 + fib_n_2
    return output

p = fibonacci_no(4)
print(p)
