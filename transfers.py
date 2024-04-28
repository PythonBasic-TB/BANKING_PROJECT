from  test_database import customers as database
from validator import validate_iban, validate_input_is_float

def transfer_money():
    iban1 = input("Enter sender's IBAN: ")
    
    if not validate_iban(iban1):
        print(f"Invalid IBAN {iban1}")
        return
    
    iban2 = input("Enter receiver's IBAN: ")
    
    if not validate_iban(iban2):
        print(f"Invalid IBAN {iban2}")
        return
    
    amount = input("Enter amount to transfer: ")
    if not validate_input_is_float(amount):
        print("Amount must be a number")
        return
    else:
        amount = float(amount)
        
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
