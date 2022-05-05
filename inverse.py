def square(x):
    return x * x

def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def inverse(f):
    """Return g(y) such that g(f(x)) = x"""
    return lambda y: search(lambda x: f(x) == y)

sqrt = inverse(square)
print(sqrt(25))