# Qn 1 Accept numbers from a user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
mult = num1 * num2
print(mult)

# Qn 2 Display three string “Name”, “Is”, “James” as “Name**Is**James”
print('Name', 'Is', 'James', sep='**')

# Qn 3 Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)

# Qn 4 Display float number with 2 decimal places using print()
num = 458.541315
print('%.2f' % num)

# Qn 5 Accept a list of 5 float numbers as an input from the user
numbers = []
for i in range(0, 5):
    num = input("Enter number: ")
    numbers.append(num)
print("User list: ", numbers)

# Qn 6: Write all content of a given file into a new file by skipping line number 5
# reading test.txt
with open('test.txt', 'r') as file:
    lines = file.readlines()
# open new file in write mode
with open('new_file.txt', 'w') as file:
    counter = 0
    for i in lines[0:]:
        if counter == 4:
            # skip fifth line
            counter += 1
            continue
        else:
            # write current line
            file.write(i)
            counter += 1

# Qn 7: Get multiple inputs from a user in one line
name1, name2, name3 = input("Enter 3 names separated by a space: ").split
print('Name1: ', name1)
print('Name2: ', name2)
print('Name3: ', name3)

# Qn 8: Format strings using string.format() method
totalMoney = 1000
quantity = 3
price = 450
statement = "I have {2} dollars so I can buy {0} footballs at {1:.2} dollars"
print(statement.format(quantity, price, totalMoney))

# Qn 9: Check if file is empty or not
import os

size = os.stat('test.txt').st_size
if size == 0:
    print("File is empty.")

# Qn 10: Read line number 4 from the test.txt file
with open('test.txt', 'r') as file:
    lines = file.readlines()
print(lines[3])



