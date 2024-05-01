def hist(*lists):
    appearance = []
    iban= iban= input ("Please enter you IBAN: ")
    for lst in lists:
        for entry in lst:
            if iban in entry:
                appearance.append(entry[iban])
    if appearance:
        print(f"amonatesri '{iban}': {appearance}")
    else:
        print(f"there is no information for '{iban}'in database")