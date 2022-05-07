# Representing pairs using lists (for instance, representing rational numbers)
pair = [1,2]
# "Unpacking" the list into its values (x is binded to zeroth value, y is binded to first value)
x, y = pair
# You can index into the list too (selector function)
pair[0]

# Representing rational numbers
# We want rational numbers to be in their lowest terms, hence we need a common divisor. In this case, there is a built in function called gcd (greatest common divisor), which finds the gcd between two numbers.
from fractions import gcd

# Constructor function ie. in the list form
def rational(n, d):
    # Construct a rational number x that represents n/d
    g = gcd(n, d)
    return [n//g, d//g] 

def numer(x):
    return x[0]

def denom(x):
    return x[1]

# Arithmethic implementation of rational numbers

def mul_rational(x, y):
    return [numer(x) * numer(y), denom(x) * denom(y)]

def add_rational(x, y):
    nx, dy = numer(x), denom(y)
    dx, ny = denom(x), numer(y)
    return [nx * dy + ny * dx, dx * dy]

def equal_rational(x, y):
    return numer(x) * denom(y) == denom(x) * numer(y)

# VIOLATING ABSTRACTION BARRIERS: DO NOT WRITE CODE THAT CROSSES ABSTRACTION BARRIERS!
# For instance, if I want to use add_rational(x, y), x and y input shld be rational numbers, NOT in their constructors!
# Another instance, if I want to define a function divide_rational(x, y), return value shld NOT include selectors! They shld be in the form of constructors (ie rational(x, y))


# Lesson 2: Data Representations
def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        if name == 'd':
            return d
    return select

def numer(x):
    return x('n')
    # This means numer(rational(select('n')))

def denom(y):
    return y('d')
    # This means denom(rational(select('d')))
