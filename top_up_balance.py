
def top_up (database, top_up_history):
    iban = input ("please enter your Iban: ")
    amount = float(input("please enter the amount you want to add to balance: "))
    for user_acount in database:
        if iban in user_acount:
            user_acount[iban]['balance'] += amount
            top_up_history.append(f"Toped up Balance {amount}")
            print(f"Top up is successfull")
        #print (top_up_history)
        else:
            print ('Account was not found')
        
#top_up_history = []
#database = [{'TB0001': {'name': 'Customer 1', 'surname': 'Doe', 'balance': 100, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0003': {'name': 'Customer 3', 'surname': 'Doe', 'balance': 300, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0004': {'name': 'Customer 4', 'surname': 'Doe', 'balance': 400, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0005': {'name': 'Customer 5', 'surname': 'Doe', 'balance': 500, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0006': {'name': 'Customer 6', 'surname': 'Doe', 'balance': 600, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0007': {'name': 'Customer 7', 'surname': 'Doe', 'balance': 700, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0008': {'name': 'Customer 8', 'surname': 'Doe', 'balance': 800, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0009': {'name': 'Customer 9', 'surname': 'Doe', 'balance': 900, 'loan': 0, 'interest': 8.2}}, 
             #{'TB0010': {'name': 'Customer 10', 'surname': 'Doe', 'balance': 1000, 'loan': 0, 'interest': 8.2}}, 
             #{'TB7133': {'name': 'otar', 'surname': 'kharatishvili', 'balance': 102931, 'loan': 0, 'interest': 8.2}}]

#top_up(database, 50, top_up_history)
#print(database)
#print(top_up_history)