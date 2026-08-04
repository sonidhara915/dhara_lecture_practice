print("-"*20)
print("Bankaccount project")
print("-"*20)

class BankAccount:

    def __init__(self,name,balance):

        self.name = name
        self.balance = balance

    def Chack_balance(self):

        print("Current balace:",self.balance)

    def diposite(self):

        self.balance += amount

        print("Diposite amount sucessfully!")

    def withdraw(self):

        if amount <= self.balance:

            self.balance -= amount
        else:
            print("please chake your balance")

name = input("enter your name:")
balance = float(input("Enter your opening balance:"))
account = BankAccount(name,balance)

while True:

    print("1.chack balance")
    print("2.diposite")
    print("3.withdraw")
    print("4.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        account.Chack_balance()
    elif choice == 2:
        amount = float(input("Enter your diposite amount:"))
        account.diposite(amount)
    elif choice == 3:
        amount = float(input("Enter your withdraw amount:"))
        account.withdraw(amount)
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
