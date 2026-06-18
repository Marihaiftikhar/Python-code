import random
import string
length = input("enter the length of passward:")
if length =="":
      length =8
else:
     length = int(length)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_characters = lower + upper +digits +symbols
passward =""
for i in range(length):
    passward+=random.choice(all_characters)
print("generated passward is:",passward)