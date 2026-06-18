import random
secret_number = random.randint(1,10)
guess = int(input("Enter the number "))
while guess != secret_number:
    if guess < secret_number:
        print("high value.")
    else:
        print("low value.")
    guess = int(input("Enter the number "))
print("congradulations!")