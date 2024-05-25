from accaunt_data import account_database as database
from find_customer_with_iban import find_customer_with_iban
from validator import validate_iban
def view_acc(database):
    iban = input("Enter account's IBAN: ")
    
    if not validate_iban(iban):
        print(f"Invalid IBAN {iban}")
        return
    account = find_customer_with_iban(iban)
    if not account:
        print(f"Account {iban} does not exist")
    else:
        
        print(f"Account details for {iban}")
        for key in account:
            print(f"{key}: {account[key]}")

 
              
# view_acc(database)