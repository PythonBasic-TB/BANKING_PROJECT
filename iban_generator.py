import random

def generate_iban(user_acount):
	while True:
		iban =  "TB" + ''.join(random.choices('0123456789', k=4))
		if iban not in user_acount:
			return iban