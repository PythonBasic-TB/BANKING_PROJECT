from  test_database import customers as database

def transfer_money(iban1, iban2, amount):
    
    if iban1 not in database:
        print(f"Account {iban1} does not exist")
        
    elif iban2 not in database:
        print(f"Account {iban2} does not exist")
        
    elif database[iban1]['balance'] < amount:
        print(f"Insufficient balance on account {iban1}")
        
    else:
        print(f"\nThe balance on account {iban1} is {database[iban1]['balance']} GEL")
        print(f"The balance on account {iban2} is {database[iban2]['balance']} GEL")
        database[iban1]['balance'] -= amount
        database[iban2]['balance'] += amount
        print(f"\nTransfer of {amount} GEL from {iban1} t0 {iban2} was successful")
        print(f"\nThe balance on account {iban1} is {database[iban1]['balance']} GEL")
        print(f"The balance on account {iban2} is {database[iban2]['balance']} GEL")


