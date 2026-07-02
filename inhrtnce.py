class Bank:
    def __init__(self,name,acc,balance,branch):
        self.name=name
        self.acc=acc
        self.balance=balance
        self.branch=branch

   # def get_acc(self):
    #    return self.acc

        if balance>500:
            print("balance is ok")
        else:
            print("balance is low")

    def acc_holder(self):
        print(f"welcome {self.name} to our banking application.your acc balance is {self.balance+100} and ur branch is {self.branch}")   #abstraction

branch1="januganj"
branch2="balasore"


a1=Bank("bisa",123,600,branch1)
print(a1.name,a1.acc,a1.balance)
a2=Bank("gudu",1345,500,branch2)
print(a2.name,a2.acc,a2.balance)
print(a1.__dict__)
a1.acc_holder()
a2.acc_holder()


#child class---------------
class Branch(Bank):
    def __init__(self,name,acc,balance,branch,loan):
        super().__init__(name,acc,branch,balance)
        self.loan=loan

    def acc_holder(self):
        super().acc_holder()

a3=Branch("andu",2222,800,"yes")
print(a3.loan)
a3.acc_holder()



