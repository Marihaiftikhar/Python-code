
class ATM_machine:
    def __init__(self, balance,PIN):
        self.balance =balance
        self.PIN =PIN
        self.transaction = []
        # method to verify pin
    def verifyPIN(self,enteredpin):
        return enteredpin == self.PIN
    # deposit method
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transaction.append(f"deposited {amount}")
            print("the deposited amount is",amount)
            # withdraw method
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            self.transaction.append(f"withdraw {amount}")
            print("the  withdraw amount is:",amount)
        else:
            print("amount is greater than balance:")
            # check balance method
    def check_balance(self):
        print("the total balance is",self.balance)
        # show transaction 
    def show_transaction(self):
        print("transaction history:")
        for transaction in self.transaction:
            print(transaction)
            # create object of ATM_machine class
atm = ATM_machine(5000,1234)
enteredpin = int(input("enter your pin:"))
if atm.verifyPIN(enteredpin):
    while True:
        print("1.Deposit")
        print("2.withdraw")
        print("3.check balnace")
        print("4.transactions")
        print("5.exit")
        
        choice = int(input("enter your choice:"))
        if choice == 1:
           amount = float(input("the the amount you want to deposit:"))
           atm.deposit(amount)
        elif choice ==2:
           amount = float(input("enter the amount you want to withdraw:"))
           atm.withdraw(amount)
        elif choice ==3:
           atm.check_balance()
        elif choice == 4:
           atm.show_transaction()
        elif choice == 5:
            print("Thank You")
            break
        else:
            print("invalid choice:")
else:
    print("wrong pin:")
        
        
     

    
     
    
    
        
        
     
        
    
        
    


