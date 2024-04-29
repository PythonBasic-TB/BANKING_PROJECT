from test_database import customers

def find_user_with_iban(iban):
    for customer in customers:
        if customer.get(iban):
            return customer
    return None


print(find_user_with_iban("TB0001"))

