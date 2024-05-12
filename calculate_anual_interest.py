from validator import validate_iban, validate_input_is_float, validate_iban_exists
from add_loan_to_balance import add_loan
from find_customer_with_iban import find_customer_with_iban
import csv

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
    
        with open('loanInformation.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            monthlyRate = (loan + annualRate)/12
            for i in range(1,13):
                writer.writerow([i,monthlyRate])
        
    elif answer.upper() == "NO":
        return
    else:
        print("Invalid answer")
        return



    


    