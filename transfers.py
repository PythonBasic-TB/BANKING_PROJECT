from accaunt_data import account_database as database
from validator import validate_iban, validate_input_is_float, validate_iban_exists
from find_customer_with_iban import find_customer_with_iban
def transfer_money(database):
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
    sender = find_customer_with_iban(iban1)
    receiver = find_customer_with_iban(iban2)    
    if not sender:
        print(f"Account {iban1} does not exist")
        
    elif not receiver:
        print(f"Account {iban2} does not exist")
        
    elif sender['balance'] < amount:
        print(f"Insufficient balance on account {iban1}")
        
    else:
        print(f"\nThe balance on account {iban1} is {sender['balance']} GEL")
        print(f"The balance on account {iban2} is {receiver['balance']} GEL")
        sender['balance'] -= amount
        receiver['balance'] += amount
        print(f"\nTransfer of {amount} GEL from {iban1} t0 {iban2} was successful")
        print(f"\nThe balance on account {iban1} is {sender['balance']} GEL")
        print(f"The balance on account {iban2} is {receiver['balance']} GEL")


# transfer_money(database)