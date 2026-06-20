import random
choice =["rock","paper","scissors"]
user = input("enter your choice: ").lower()
computer = random.choice(choice)
print("computer chose:",computer)
if user == computer:
    print("its  a draw")
elif user =="rock" and computer =="scissors":
    print("you win")
elif user =="paper" and computer =="rock":
    print("you win")
elif user =="scissors" and computer =="paper":
    print("you win")
elif computer =="rock" and user =="scissors":
    print("computer wins win")  
elif computer =="paper" and user =="rock":
    print("computer wins win")     
elif computer =="scissors" and user =="paper":
    print("computer wins win")     
else:
    print("invalid input")
    