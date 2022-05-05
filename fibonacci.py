def fib(n):
    pred, curr = 0, 1
    counter = 1
    while counter < n:
        pred, curr = curr, pred + curr
        counter += 1
    return curr

print(fib(5))