class account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
        else:
            print("Invalid amount")    
        
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f'{self.balance}'

maazin=account("maazin",20000)
adil=account("adil",30000)


print(maazin)
maazin.withdraw(2000)
print(maazin)