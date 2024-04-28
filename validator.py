def validate_iban(iban):
    if iban[:2 ] != "TB":
        return False
    if len(iban) != 6:
        return False
    if not iban[2:].isdigit():
        return False
    return True
    

def validate_balance ():
    pass

def validate_name():
    pass

def validate_input_is_float(input_data):
    try:
        float(input_data)
        return True
    except ValueError:
        return False