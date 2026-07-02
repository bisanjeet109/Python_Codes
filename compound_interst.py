"""COMPOUND INTERST
Amount=p(1+R/100)**T
compound interest= Amount-p

"""
principal=float(input("enter the principal amount:"))
rate=float(input("enter the rate of interest:"))
time=float(input("enter the time of interest:"))
amount=(principal*(1+rate/100)**time)
print("amount=",round(amount,2))
compound_interest=amount-principal
print("ci=",round(compound_interest,2))
