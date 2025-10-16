class bankaccount():
           def __init__(self,accno,accname,acctype,balance):
                      self.accno=accno
                      self.accname=accname
                      self.acctype=acctype
                      self.balance=balance
           def deposite(self,amount):
                      self.balance+=amount
                      print("Current Balance is=",self.balance)
                      print("Deposited Amount is",amount)
           def accountinfo(self):
                      print("Account Number=",self.accno)
                      print("Account Number=",self.accname)
                      print("Account Number=",self.acctype)
                      print("Account Number=",self.balance)
           def withdraw(self,amount):
                      if amount>self.balance:
                         print("insufficient balance!")
                      else:
                                 self.balance-=amount
                                 print("withdrawn:" ,amount,"|remaining balance:",self.balance)
              
acno=int(input("enter your account number:"))
name=input("enter the account name:")
actype=input("enter the amount type:")
bal=float(input("enter the balance:"))
obj=bankaccount(acno,name,actype,bal)
print("account information=",obj.accountinfo())

depamount=int(input("enter the amount to be deposited:"))
obj.deposite(depamount)

wid=int(input("enter the withdrawal amount:"))
obj.withdraw(wid)

                      
