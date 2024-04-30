
def generate_iban(database):
	ibans = [iban for user in database for iban in user.keys()]

	for i in range(1, 10000):
		iban = f"TB{i:04d}"
		if iban not in ibans:
			return iban
	raise ValueError("Iban limit reached(TB9999)")



database = [{'TB0001': {'name': 'Customer 1', 'surname': 'Doe', 'balance': 100, 'loan': 0, 'interest': 8.2}}, 
            {'TB0002': {'name': 'Customer 2', 'surname': 'Doe', 'balance': 200, 'loan': 0, 'interest': 8.2}}, 
            {'TB0003': {'name': 'Customer 3', 'surname': 'Doe', 'balance': 300, 'loan': 0, 'interest': 8.2}}, 
            {'TB0004': {'name': 'Customer 4', 'surname': 'Doe', 'balance': 400, 'loan': 0, 'interest': 8.2}}, 
            {'TB0005': {'name': 'Customer 5', 'surname': 'Doe', 'balance': 500, 'loan': 0, 'interest': 8.2}}]

iban = generate_iban(database)
print(iban)