def get_numbers_ticket(min = 1, max = 5, quantity = 1):
    import random
    if min <= 0 or max <= 0 or quantity > (max - min + 1):
        return []
    else:
        all_lottery_numbers = tuple(range(min, max + 1))
        win_numbers = random.sample(all_lottery_numbers, quantity)
        return sorted(win_numbers)

lotery_tickets = get_numbers_ticket(1, 1000, 2)
print("Numbers:", lotery_tickets)