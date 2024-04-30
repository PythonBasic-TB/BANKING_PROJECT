from validator import validate_iban, validate_input_is_float, validate_iban_exists
from add_loan_to_balance import add_loan
from find_customer_with_iban import find_customer_with_iban

def cal_anual_int (database, loan_hist):
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
    
    accountInfo = find_customer_with_iban(iban)
    
    annualRate = loan * accountInfo['interest'] / 100
    print(f"Your annual interest rate will be {annualRate} GEL")
    answer = input("Proceed with loan Yes/No: ")
    if answer.upper() == "YES":
        add_loan(loan, accountInfo, loan_hist, iban)
    elif answer.upper() == "NO":
        return
    else:
        print("Invalid answer")
        return



    


    