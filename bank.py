class Bank:
    acc_name = ""
    acc_no = ""
    acc_type = ""
    acc_balance = 0

    def __init__(self, a_name, a_no, a_type, a_balance):
        self.acc_name = a_name
        self.acc_no = a_no
        self.acc_type = a_type
        self.acc_balance = a_balance

    def deposit(self, a_deposit):
        print("Initial balance is  : ", self.acc_balance)
        print("Deposit amount is  : ", a_deposit)
        self.acc_balance += a_deposit
        print("Current balance is  : ", self.acc_balance)

    def withdraw(self):
        print("Current balance is  : ", self.acc_balance)
        self.amount = int(input("How much amount do you need to withdraw? : "))
        if self.amount > self.acc_balance:
            print("You don't have enough balance to withdraw!!")
            print("Current balance is  : ", self.acc_balance)
        else:
            print(self.amount, " has been withdrawn.")
            self.acc_balance -= self.amount
            print("Current balance is  : ", self.acc_balance)

    def acc_info(self):
        print(".........................................................")
        print("Account holder name    :  ", self.acc_name)
        print("Account number         :  ", self.acc_no)
        print("Account type           :  ", self.acc_type)
        print("Account Balance        :  ", self.acc_balance)
        print(".........................................................")


def main():
    name = input("Enter Account holder name : ")
    no = input("Enter Account number        : ")
    atype = input("Enter Account type          : ")
    bal = int(input("Enter Account initial balance : "))
    holder = Bank(name, no, atype, bal)

    while True:
        print(".........................................................")
        opt = int(input("1) Deposit \n2) Withdraw \n3) Account info \n0) Exit\nChoose your option :: "))
        print(".........................................................")

        if opt == 1:
            amount = int(input("Deposit amount : "))
            holder.deposit(amount)
        elif opt == 2:
            holder.withdraw()
        elif opt == 3:
            holder.acc_info()
        elif opt == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid Option! Please try again.")


if __name__ == "__main__":
    main()