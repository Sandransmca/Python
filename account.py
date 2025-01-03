class Account:
    def __init__(self,account_number,name,acc_type,balance=0):
        self.account_number=account_number
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print("deposited" ,amount, "balance is",self.balance)
        else:
            print("deposited amount is positive")

    def withdraw(self,amount):
        if amount >0:
            if amount <= self.balance:
                self.balance -= amount
                print("withdrew",amount,"new balance is :",self.balance)
            else:
                print("INSUFFICIENT AMOUNT!!!!!!!!!!!!")

    def display_balance(self):
        print("Account balance:", self.balance)

def main():
    acc1=Account("100200400589","mizhi","savings",10000)
    while True:
        print("\nMenu:")
        print("1. Deposit money")
        print("2. Check balance")
        print("3.withdraw cash")
        print("4. Exit")
        choice=int(input("enter a choice: "))
        if choice==1:
            a=int(input("enter the amount: "))
            acc1.deposite(a)
        elif choice==2:
            acc1.display_balance()
        elif choice==3:
            a=int(input("Enter the amount to withdraw: "))
            acc1.withdraw(a)
        elif choice==4:
            print("Thank You.. :)")
            break
        else:
            print("invalid choice........")

main()

