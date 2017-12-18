class Bank():
    i=0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.acctnumber = Bank.i
        Bank.i += 1

    def withdraw (self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance -= amount

    def __str__(self):
        return "Account's owner is %.2f, account number is %.2f, account balance is %.2f, if you withdraw money you will have %.2f, if you withdraw money you will have %.2f" % (self.x, self.y, self.withdraw, self.deposit)
