from iban_generator import generate_iban
from accaunt_data import account_database
from validator import validate_input_is_float

def add_acount (account_database):
    user_acount ={}
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    balance = float(input("Please enter your balance, maximum 100GEL: "))
    loan = int(0)
    if not validate_input_is_float(balance):
        print("Input must be only numbers.")
        return
    else:
        balance = float(balance)
    if balance <= 100:
        iban = generate_iban(account_database)
        user_acount[iban] = {"name": name, "surname":surname, "balance": balance, "loan": loan,"interest": 8.2}
        account_database.append(user_acount)
        print ((f"Account created successfully! Account Holder: {name} {surname}, Acount number: {iban}, Balance : {balance}GEL"))
        print (account_database)
    
    return account_database
    
   