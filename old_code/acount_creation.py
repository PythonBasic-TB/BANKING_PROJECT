from iban_generator import generate_iban
from accaunt_data import account_database
from validator import validate_input_is_float
import csv

def generate_UID(iban, name, surname): #დასაკორექტირებელი მაქვს, რომ უნიკალური იყოს. IBAN-ს + იანიციალები არ გამოვა.
    
    uid = f"{iban}{name[0]}{surname[0]}" 
	
    return uid
	

def write_to_file (dictionary):
    filename='users.csv'
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dictionary)
        
        
        return filename
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
        
        user = {}
        user_id = generate_UID(iban, name, surname)
        user[user_id] = {"iban" : iban, "name": name, "surname":surname, "balance": balance, "loan": loan,"interest": 8.2}
        
        write_to_file([user])
        print ((f"Account created successfully! Account Holder: {name} {surname}, Acount number: {iban}, Balance : {balance}GEL"))
        print (account_database)
    
    return account_database
    
   