import random


def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= 1000):
        return []
    if not (1 <= max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):
        return []

    numbers = random.sample(range(min, max +1), quantity)
    numbers.sort()
    return numbers


min, max, quantity = int(input()), int(input()), int(input())
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)