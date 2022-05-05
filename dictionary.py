customer = {
    "name": "Kevin Liew",
    "age": "19",
    "is verified": True
}

customer["birthdate"] = "22 September 2002"
print(customer["birthdate"])


numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five", 
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

number = input("Phone: ")
output = ""
for ch in number:
    # If list doesn't have that value, we can make it use the ! by default instead
    # Create an output string
    output += numbers.get(ch, "!") + " "

print(output)
