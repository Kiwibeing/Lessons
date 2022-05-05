def sum_naturals(n):
    """Return the sum of N natural numbers"""
    total, k =  0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Return the sum of the first N cubes of natural numbers"""
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)
    
"""Define a function that can sum up to the nth number according to a formal parameter that would be bound to a function, called term"""
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        """What is different compared to the previous functions created? It is the repetition of doing total + __, we can eliminate by writing here total + term()"""
        """The function bound to the term gets called here"""
        total, k = total + term(k), k + 1
    return total

"""New functions look like this now:"""
def sum_cubes(n):
    return summation(n, cube)

def sum_naturals(n):
    return summation(n, identity)