from iban_generator import generate_iban
from test_database import customers

def add_acount (customers):
    user_acount ={}
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    balance = int(input("Please enter your balance, at least 100GEL: "))
    loan = int(0)
    interest = float(8.2)
    if balance>= 100:
        iban = generate_iban(customers)
        user_acount[iban] = {"name": name, "surname":surname, "balance": balance, "loan": loan,"interest": interest}
        customers.append(user_acount)
        print ((f"Account created successfully! Account Holder: {name} {surname}, Acount number: {iban}, Balance : {balance}GEL"))
        print (customers)
    
    return customers
    

#database = [{'TB0001': {'name': 'Customer 1', 'surname': 'Doe', 'balance': 100, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0002': {'name': 'Customer 2', 'surname': 'Doe', 'balance': 200, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0003': {'name': 'Customer 3', 'surname': 'Doe', 'balance': 300, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0004': {'name': 'Customer 4', 'surname': 'Doe', 'balance': 400, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0005': {'name': 'Customer 5', 'surname': 'Doe', 'balance': 500, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0006': {'name': 'Customer 6', 'surname': 'Doe', 'balance': 600, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0007': {'name': 'Customer 7', 'surname': 'Doe', 'balance': 700, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0008': {'name': 'Customer 8', 'surname': 'Doe', 'balance': 800, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0009': {'name': 'Customer 9', 'surname': 'Doe', 'balance': 900, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0010': {'name': 'Customer 10', 'surname': 'Doe', 'balance': 1000, 'loan': 0, 'interest': 8.2}}]
#add_acount(database)
   