#from accaunt_data import top_up_hist
#from accaunt_data import loan_hist
#from accaunt_data import p2p_hist
from accaunt_data import t_h
#account_database = [
   # {'TB0001': {'name': 'Customer 1', 'surname': 'Doe', 'balance': 100, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0002': {'name': 'Customer 2', 'surname': 'Doe', 'balance': 200, 'loan': 0, 'interest': 8.2}}, 
   # {'TB0001': {'name': 'Customer 3', 'surname': 'Doe', 'balance': 300, 'loan': 0, 'interest': 8.2}},
   # ]


def view_history (t_h):
    iban = input ("Please enter you IBAN: ")
    type = input ("please enter what type of transaction you want to find (top_up, transactions, or loan :  )").lower()
    for ibans in t_h:
            if iban  in ibans:
                for k, v in ibans.items():
                    if k== iban and type in str(v):
                        print (f"{k}:{v}")


