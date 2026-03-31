memo = [None] * 100
counter = 0


def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

n = 10

print(f'Fib of {n} = {fib(n)}')
print(f'function calls = {counter}')

"""
here BigO is (2n-1)
"""