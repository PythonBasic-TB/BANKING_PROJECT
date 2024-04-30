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
    
database = [{'TB0001': {'name': 'Customer 1', 'surname': 'Doe', 'balance': 100, 'loan': 0, 'interest': 8.2}}, 
    {'TB0002': {'name': 'Customer 2', 'surname': 'Doe', 'balance': 200, 'loan': 0, 'interest': 8.2}}, 
    {'TB0003': {'name': 'Customer 3', 'surname': 'Doe', 'balance': 300, 'loan': 0, 'interest': 8.2}}, 
    {'TB0004': {'name': 'Customer 4', 'surname': 'Doe', 'balance': 400, 'loan': 0, 'interest': 8.2}}, 
    {'TB0005': {'name': 'Customer 5', 'surname': 'Doe', 'balance': 500, 'loan': 0, 'interest': 8.2}}, 
    {'TB0006': {'name': 'Customer 6', 'surname': 'Doe', 'balance': 600, 'loan': 0, 'interest': 8.2}}, 
    {'TB0007': {'name': 'Customer 7', 'surname': 'Doe', 'balance': 700, 'loan': 0, 'interest': 8.2}}, 
    {'TB0008': {'name': 'Customer 8', 'surname': 'Doe', 'balance': 800, 'loan': 0, 'interest': 8.2}}, 
    {'TB0009': {'name': 'Customer 9', 'surname': 'Doe', 'balance': 900, 'loan': 0, 'interest': 8.2}}, 
    {'TB0010': {'name': 'Customer 10', 'surname': 'Doe', 'balance': 1000, 'loan': 0, 'interest': 8.2}}]
add_acount(database)
   