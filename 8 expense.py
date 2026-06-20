expenses =[]
while True:
    category = input("enter category(food,transport,shopping):")
    amount = float(input("enter amount:"))
    expense = {
        "category": category,
        "amount":amount
    }
    
    expenses.append(expense)
    with open("expense.txt","a") as f:
        f.write(category +":"+ str(amount) +"\n")
        choice = input("add another expense?(y/n):")
        if choice.lower() !="y":
            break
    total =0
    
    for expense in expenses:
        print(expense["category"],"-",expense["amount"])
        total +=expense["amount"]
        print("total expense=",total)
    