
def top_up (iban, user_acount, amount, top_up_history):
    if iban in user_acount:
        user_acount[iban]['balance'] += amount
        top_up_history.append(f"Toped up Balance {amount}")
        print(f"Top up is successfull")
        #print (top_up_history)
    else:
        print ('Account was not found')
    


