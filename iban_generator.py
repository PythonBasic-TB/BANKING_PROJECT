
def generate_iban(database):
	ibans = [iban for user in database for iban in user.keys()]

	for i in range(1, 10000):
		iban = f"TB{i:04d}"
		if iban not in ibans:
			return iban
	raise ValueError("Iban limit reached(TB9999)")



