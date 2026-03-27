class adp:
    def __init__(self):
        self.acc = 0
        self.balance = 0

    def account(self , x):
        x= int(input("Enter your acc number: "))
        x = self.acc
        return x
    
    def deposit(self):
        depo = int(input("enter your amount to deposit: "))
        self.balance + depo = self.balance
    
    def bal(self):
        return self.balance 
    
    def withdrawl(self):
        withdraw = int(input("enter your amount to withdraw: "))
        if withdraw >= self.balance:
            self.balance - withdraw = self.balance
            return self.balance
        else :
            print("not sufficient amount")
            


