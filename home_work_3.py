raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    import re
    list_of_pure_numbers=[]
    for number in phone_number:
        cleared_number = re.sub(r"\D","", number)
        if len(cleared_number) == 10:
            cleared_number = "+38"+ cleared_number
            list_of_pure_numbers.append(cleared_number)
        elif len(cleared_number) == 12:
            cleared_number = "+" + cleared_number
            list_of_pure_numbers.append(cleared_number)
        else:
            print(f"Not enough digits in telephone number {number}")
    return list_of_pure_numbers

print("Нормалізовані номери телефонів для SMS-розсилки:", normalize_phone(raw_numbers))

