def presence_check(field):
    return len(field) != 0

def length_check(field, min_length):
    return len(field) >= min_length

def complexity_check(field, lower=False, upper=False, digit=False, special=False):
    valid = True
    if lower and field.upper() == field:
        valid = False
    if upper and field.lower() == field:
        valid = False
    if digit and "".join([char for char in field if char.isalpha()]) == field:
        valid = False
    if special and "".join([char for char in field if char.isalnum()]) == field:
        valid = False
    return valid
