from validator import validate_iban, validate_input_is_float, validate_iban_exists
from add_loan_to_balance import add_loan
from acount_creation import interest

def cal_anual_int (database, interest):
    iban = input("Enter sender's IBAN: ")
    if not validate_iban(iban):
        print(f"Invalid IBAN {iban}")
        return
    
    if not validate_iban_exists(iban, database):
        print(f"Account {iban} does not exist")
        return

    loan = input("Enter the loan amount: ")
    if not validate_input_is_float(loan):
        print("Loan amount must be a number")
        return
    else:
       loan = float(loan)
    
    annualRate = loan * interest / 100
    print(f"Your annual interest rate will be {annualRate}")
    answer = input("Proceed with loan Yes/No: ")
    if answer.capitalize == "YES":
        add_loan(database, iban, loan)
    elif answer.capitalize == "NO":
        return
    else:
        print("Invalid answer")
        return



    


    