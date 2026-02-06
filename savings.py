class Account:
    def __init__(self,account_holder: str,_balance: float) -> None:  
        self.account_holder=account_holder
        self._balance=_balance

    def deposit(self,amount: float) -> None: 
        if amount>=0:
            self._balance+=amount
        else:
            print("Invalid amount")    
        
    def withdraw(self,amount: float) -> None:
        if amount<=self._balance:
            self._balance-=amount
        else:
            print("Insufficient balance")

    def __str__(self) -> str:
        return f'{self._balance}'



class SavingsAccount(Account):
    def __init__(self,account_holder: str,_balance: float,interest: float) -> None:
        super.__init__(account_holder,_balance)
        self.interest=interest    

    def apply_interest(self) -> None:
        self._balance+=self._balance*self.interest
        print(f'Interest applied.New balance {self._balance}')

maazin=SavingsAccount("Maazin",1000,0.05)
maazin.apply_interest()