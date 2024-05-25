from accaunt_data import account_database as database
#from accaunt_data import p2p_hist
from accaunt_data import t_h
from add_history_to_file import add_to_file
from validator import validate_iban, validate_input_is_float, validate_iban_exists
from find_customer_with_iban import find_customer_with_iban
def transfer_money(database):
    
    iban1 = input("Enter sender's IBAN: ")
    
    if not validate_iban(iban1):
        print(f"Invalid IBAN {iban1}")
        return
    s= iban1
    iban2 = input("Enter receiver's IBAN: ")
    
    if not validate_iban(iban2):
        print(f"Invalid IBAN {iban2}")
        return
    y=iban2
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
        ibans = {}
        ibans2 ={}
        f='transactions.txt'
        print(f"\nThe balance on account {iban1} is {sender['balance']} GEL")
        print(f"The balance on account {iban2} is {receiver['balance']} GEL")
        sender['balance'] -= amount
        if s not in ibans:
            ibans[s] = []
            ibans[s].append(f"{sender['name']} {sender['surname']} transfer -{amount}")
            t_h.append(ibans)
            add_to_file (t_h, f)
            
        receiver['balance'] += amount
        
        if y not in ibans2:
            ibans2[y] = []
            ibans2[y].append(f"{receiver['name']} {receiver['surname']} transfer +{amount}")
            t_h.append(ibans2)
            add_to_file (t_h, f)
        print (t_h)
        print(f"\nTransfer of {amount} GEL from {iban1} t0 {iban2} was successful")
        print(f"\nThe balance on account {iban1} is {sender['balance']} GEL")
        print(f"The balance on account {iban2} is {receiver['balance']} GEL")
    print (t_h)

# transfer_money(database)