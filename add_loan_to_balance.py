def add_loan(database, iban, loan):
    database[iban]['balance'] += loan
    database[iban]['loan'] -= loan
    print (f"The loan has been issued successfully. Your balance was filled with {loan} GEL")