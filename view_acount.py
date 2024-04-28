from  test_database import customers as database
from validator import validate_iban
def view_acc():
    iban = input("Enter account's IBAN: ")
    
    if not validate_iban(iban):
        print(f"Invalid IBAN {iban}")
        return
    if iban not in database:
        print(f"Account {iban} does not exist")
    else:
        print(f"Account details for {iban}")
        print(f"Name: {database[iban]['name']}")
        print(f"Surname: {database[iban]['surname']}")
        print(f"Balance: {database[iban]['balance']} GEL")
        print(f"Loan: {database[iban]['loan']} GEL")
        print(f"Interest Rate: {database[iban]['interest']}%")
 
              
