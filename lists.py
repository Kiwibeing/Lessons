names = ['John', 'Mary', 'Sarah', 'Tim', 'Mary']
print(names[2:5])

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# List Comprehensions
list = [1, 3, 5, 7, 9]

# I want to create a new list by adding 1 to each element
new_list = [x+1 for x in list]

# I want to create a new list for numbers that divide evenly with 25
new_list = [x for x in list if 25 % x == 0]

# Divisors + addition of lists
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]
