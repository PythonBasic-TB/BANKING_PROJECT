from test_database import customers
from accaunt_data import account_database

# def find_customer_with_iban(iban):
#     for customer in customers:
#         if customers.get(f"{iban}"):
#             return customers.get(f"{iban}")
#     return None

def find_customer_with_iban(iban):
    for ibans in account_database:
        if iban in ibans:
            return ibans[iban]


# def find_customer_with_iban(iban):
#     for account in account_database:
#         if account_database.get(f"{iban}"):
#             return account_database.get(f"{iban}")
#     return None

#print(find_customer_with_iban("TB0002"))

