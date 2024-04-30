

def add_loan(loan, accountInfo, loan_hist, iban):
    accountInfo['balance'] += loan
    accountInfo['loan'] -= loan
    historyElement = {'iban' : iban, 'loan' : loan}
    loan_hist.append(historyElement)
    print (f"The loan has been issued successfully. Your balance was filled with {loan} GEL")