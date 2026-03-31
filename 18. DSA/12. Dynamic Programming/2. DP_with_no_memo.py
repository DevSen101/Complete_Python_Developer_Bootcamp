# let's write fibonacci code without memoization and see in some opertaion it take so many functions call. which is very insuffeicient.

counter = 0


def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = 35

print(f'Fib of {n} = {fib(n)}')
print(f'function calls = {counter}')

