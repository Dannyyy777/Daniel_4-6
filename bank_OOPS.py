class Bank:
    def __init__(self, cash):
        self.cash = cash

    def credit(self):
        c_num = int(input("Enter an amount to credit = "))
        self.cash = self.cash + c_num
        print("Balance = ",self.cash)

    def debit(self):
        d_num = int(input("Enter an amount to debit = "))
        self.cash = self.cash - d_num
        print("Balance = ", self.cash)

num_1 = 1
num_2 = 2
cash = Bank(10000)

while num_1 == 1 or num_2 == 2:

    print("1. Credit")
    print("2. Debit")
    print("3. Exit")

    num = int(input("Enter your choice = "))

    if num == 1:
        cash.credit()
    elif num == 2:
        cash.debit()
    else:
        exit()