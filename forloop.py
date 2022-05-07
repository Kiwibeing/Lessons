prices = [10, 20 , 30]

total = 0

for price in prices:
    total += price

print(f"Total price of goods is ${total}")

# Count the number of times that value appears in the sequence s
def count(s, value):
    total = 0
    for element in s:
        if value == element:
            total += 1
    return total

# Sequence unpacking in for statements
pairs = [[1,2], [2,2], [3.2], [4,4]]
same_count = 0
# In this case, x and y are bound to the elements in each element of pairs (for fixed-length sequence)
for x, y in pairs:
    if x == y:
        same_count += 1
