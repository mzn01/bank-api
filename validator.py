import pandas as pd





class SavingsAccount:
    def __init__(self,account_holder: str,_balance: float,interest: float) ->None :
        self.account_holder = account_holder
        self._balance = _balance
        self.interest = interest

    def apply_interest(self) -> None:
            self._balance+=self._balance*self.interest
            print(f'Interest applied.New balance {self._balance}')

filename = 'data.csv'

df = pd.read_csv(filename,names=['name','balance','rate'])

df['new_balance']=df.iloc[:,1]+df.iloc[:,1]*df.iloc[:,2]
        
print(df)


