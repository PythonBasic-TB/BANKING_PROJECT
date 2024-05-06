
from accaunt_data import t_h 
def add_to_file(t_h, f):
    f = 'transactions.txt'
    try:
        with open(f, 'a') as file:
            for item in t_h:
            
             file.write(str(item) +'\n')
    except   Exception as e:
        print("Error:", e)