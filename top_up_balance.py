from accaunt_data import account_database
#from accaunt_data import top_up_hist
from add_history_to_file import add_to_file
from validator import validate_iban_exists
from accaunt_data import t_h

def top_up (account_database, t_h):
    top_up_history = {}
    iban = input ("please enter your Iban: ")
    f='transactions.txt'
    if not validate_iban_exists(iban, account_database):
        print ("Iban dosn't exist.")
    else:
        amount = float(input("please enter the amount you want to add to balance: "))
        for user_acount in account_database:
            if iban in user_acount:
                user_acount[iban]['balance'] += amount
                if iban not in top_up_history:
                    top_up_history[iban] = []
            
                    top_up_history[iban].append(f"{user_acount[iban]['name']} {user_acount[iban]['surname']} top_up {amount}")
                    t_h.append(top_up_history)
                    add_to_file(t_h, f)
                    print(f"Top up is successfull")
                    
                return
     
    




