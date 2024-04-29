import random

def generate_iban(database):
	
	while True:
		iban =  "TB" + ''.join(random.choices('0123456789', k=4))
		if iban not in database:
			return iban