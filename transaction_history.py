from accaunt_data import top_up_hist
from accaunt_data import loan_hist
from accaunt_data import p2p_hist

#account_database = [
   # {'TB0001': {'name': 'Customer 1', 'surname': 'Doe', 'balance': 100, 'loan': 0, 'interest': 8.2}}, 
    #{'TB0002': {'name': 'Customer 2', 'surname': 'Doe', 'balance': 200, 'loan': 0, 'interest': 8.2}}, 
   # {'TB0001': {'name': 'Customer 3', 'surname': 'Doe', 'balance': 300, 'loan': 0, 'interest': 8.2}},
   # ]


def view_top_up_history (top_up_hist):
    iban= input ("Please enter you IBAN: ")
    for ibans in top_up_hist:
            if iban  in ibans:
                for k, v in ibans.items():
                    if k== iban:
                        print (f"{k}:{v}")

def view_transfer_history(p2p_hist):
    iban= input ("Please enter you IBAN: ")
    for ibans in p2p_hist:
            if iban  in ibans:
                for k, v in ibans.items():
                    if k== iban:
                        print (f"{k}:{v}")
def view_loan_history(loan_hist):
    iban= input ("Please enter you IBAN: ")
    for ibans in loan_hist:
            if iban  in ibans:
                for k, v in ibans.items():
                    if k== iban:
                        print (f"{k}:{v}")
                        
