def add_loan(loan, accountInfo):
    accountInfo['balance'] += loan
    accountInfo['loan'] -= loan
    print (f"The loan has been issued successfully. Your balance was filled with {loan} GEL")