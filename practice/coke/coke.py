amount =50
while amount>0:
    print("Amount Due:",amount)
    insert= int(input("Insert Coin: "))
    if insert in [25,10,5]:
        amount-=insert
change_owed=abs(amount)
print("Change owed:",change_owed)
