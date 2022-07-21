due = 0
owed = 0
amount = 0
while True:
    coin = int(input('Insert Coin: '))
    
    if coin == 10 or coin == 5 or coin == 25:
        amount += coin
    
    if amount < 50:
        due = 50 - amount 
        print(f'Amount due: {due}')
    elif amount >= 50:
        owed = amount - 50
        print(f'Change owed: {owed}')
        break
