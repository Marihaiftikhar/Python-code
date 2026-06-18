convertor = {
    1:"km to miles",
    2:"celsius to fahrenheit",
    3:"kg to pounds",
    
    }
for key,value in convertor.items():
    print(key,":",value)
choice = int(input("enter the choice:"))
value = float(input("enter the value:"))
if choice ==1:
        print("the value in miles is:",value*0.621371)
elif choice ==2:
        print("the value in fahrenheit is:",(value*9/5)+32)
elif choice ==3:
        print("the value in pounds is:",value*2.20462)
else:
        print("invalid choice")