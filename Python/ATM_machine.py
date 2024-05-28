print("{**WELCOME TO MY BANK ATM **}")
print("")
print("-----------------------------------------------------------")

class Detail():
    def __init__(self,name ,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
    def userdetails(self):
        print(f"""
                  username -- {self.name}
                  userage  -- {self.age}
                  useradress--{self.adress}""")

class Bank(Detail):
    def __init__(self,name,age,adress,amount):
        super().__init__(name,age,adress)
        self.amount=amount
    def deposit(self):
        self.userdetails()
        deposit=int(input("*Enter deposit amount ==  "))
        self.amount=self.amount+deposit
        print(f"Total amount after deposit {self.amount}")
    def withdrow(self):
        withdrw=int(input("**Enter withdrw amount == "))
        self.amount=self.amount-withdrw
        print(f"Total amount after withdrow {self.amount}")
class final(Bank):
   
        def f(self):
             self.userdetails()
             while True:
                print("""choose any  for    
                                        deposit = 1
                                        withdrow = 2
                                        totalamount =3""")
                choice=int(input("choise here :: "))
             
                if choice==1:
                    print('you want deposit')
                    self.deposit()
                    print("----------------------------------------------")
                elif choice==2:
                    print('you want withdrow')
                    self.withdrow()
                    print("---------------------------------------------------------")
                elif choice==3:
                    print("you want total amount")
                    print(f"Total avelable amount   :: {self.amount}")
                    print("---------------------------------------------------------")
                else:
                    print("Thank for visit our ATM")
                    break

print("conform your identity")                               
print()
name=input("Enter yout name ::  ")
age=int(input("Enter yout age ::  "))
adress=input("Enter yout adress ::  ")

f=final(name,age,adress,1000)
print("-------------------------------------------------------")
f.f()
        


