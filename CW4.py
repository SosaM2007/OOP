p = int(input("Please enter principal amount="))
R = int(input("Please enter rate of interest="))
n = int(input("Please enter duration of the loan="))

r=R/(12*100)
emi = p * r * ((1+r)**n)/((1+r)**n-1)
for i in range(1,n):
    balance = p-emi
    print(balance)
    p=balance
    print("emi=", emi)
    print("balance=" , balance)
    print("==========================================")
