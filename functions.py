def greet_user():
    print(f"Hi there, {name}")
    print("Welcome aboard")


print("Start")
name = input('What is your name? ')
greet_user()
print("Finish")

def greet_user2(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user2("Kevin", "Liew")
print("Finish")
greet_user2(last_name="Liew", first_name="Kevin")