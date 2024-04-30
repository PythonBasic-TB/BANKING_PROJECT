from accaunt_data import account_database
from accaunt_data import top_up_hist
from validator import validate_iban_exists

def top_up (account_database, top_up_hist):
    top_up_history = {}
    iban = input ("please enter your Iban: ")
    
    if not validate_iban_exists(iban, account_database):
        print ("Iban dosn't exist.")
    else:
        amount = float(input("please enter the amount you want to add to balance: "))
        for user_acount in account_database:
            if iban in user_acount:
                user_acount[iban]['balance'] += amount
                if iban not in top_up_history:
                    top_up_history[iban] = []
            
                    top_up_history[iban].append(f"Toped up Balance {amount}")
                    top_up_hist.append(top_up_history)
                    print(f"Top up is successfull")
                    
                return
     
    




