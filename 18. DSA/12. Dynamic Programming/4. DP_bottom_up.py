"""
There are two ways two solve DP problems Top-Down and Bottom-Up. we see top down earlier where we solve the top function and carry it down. now se Bottom-Up where we go from bottom to upwords.
"""

counter = 0


def fib(n):
    fib_list = [0, 1]
    global counter
    for index in range(2, n + 1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]


n = 7

print(f"Fib of {n} is {fib(n)}")
print(f"function calls = {counter}")
