from  test_database import customers as database
def view_acc(iban):
    if iban not in database:
        print(f"Account {iban} does not exist")
    else:
        print(f"Account details for {iban}")
        print(f"Name: {database[iban]['name']}")
        print(f"Surname: {database[iban]['surname']}")
        print(f"Balance: {database[iban]['balance']} GEL")
        print(f"Loan: {database[iban]['loan']} GEL")
        print(f"Interest Rate: {database[iban]['interest']}%")
        
        
view_acc("TB0005")    
              
