from validator import validate_iban, validate_input_is_float, validate_iban_exists
from add_loan_to_balance import add_loan

def GetAccountInfo (iban, database):
    for ibans in database:
        if iban in ibans:
            return ibans[iban]


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
    
    accountInfo = GetAccountInfo (iban, database)
    
    annualRate = loan * accountInfo['interest'] / 100
    print(f"Your annual interest rate will be {annualRate}")
    answer = input("Proceed with loan Yes/No: ")
    if answer.capitalize == "YES":
        add_loan(loan, accountInfo)
    elif answer.capitalize == "NO":
        return
    else:
        print("Invalid answer")
        return



    


    