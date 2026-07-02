class bank:
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


a1=bank("bisa",123,600,branch1)
print(a1.name,a1.acc,a1.balance)
a2=bank("gudu",1345,500,branch2)
print(a2.name,a2.acc,a2.balance)
print(a1.__dict__)
a1.acc_holder()
a2.acc_holder()
#print(a2.get_acc())










"""print(a1.acc)
a1.acc=456             #update
print(a1.acc)

print(a1.__dict__)
del a1.balance            #delete
print(a1.__dict__)"""
