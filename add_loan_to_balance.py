def add_loan(loan, accountInfo, loan_hist, iban):
    accountInfo['balance'] += loan
    accountInfo['loan'] -= loan
    #historyElement = {'iban' : iban, 'loan' : loan}
    ibans ={}
    if iban not in ibans:
        ibans[iban]=[]
        ibans[iban].append(f"loan -{loan}")
        loan_hist.append(ibans)
        
    print (f"The loan has been issued successfully. Your balance was filled with {loan} GEL, your balance is: {accountInfo['balance']}")
    print (loan_hist)