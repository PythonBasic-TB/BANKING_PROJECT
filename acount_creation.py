from iban_generator import generate_iban

def add_acount (name, surname, balance, user_acount):
    pass
    loan = int(0)
    interest = float(8.2)
    if balance>= 100:
        iban = generate_iban()
        user_acount[iban] = {"name": name, "surname":surname, "balance": balance, "loan": loan,"interest": interest}
        print ((f"Account created successfully! Account Holder: {name} {surname}, Acount number: {iban}, Balance : {balance}GEL"))
       
        
    return user_acount
    


