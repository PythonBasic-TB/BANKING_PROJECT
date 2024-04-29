from test_database import customers,users


# def find_user_with_iban(iban):
#     for user in users:
#         if user.get("iban"):
#             return user
#     return None



def find_customer_with_iban(iban):
    for customer in customers:
        if customers.get(f"{iban}"):
            return customers.get(f"{iban}")
    return None

