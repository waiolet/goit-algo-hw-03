from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.fromisoformat(date).date()
        today = datetime.today().date()
        return (input_date - today).days
    except ValueError:
        print("Неправильний формат дати")
        return None


while True:
    date = input("Введіть дату у форматі YYYY-MM-DD: ")
    result = get_days_from_today(date)

    if result is not None:
        print(f"Кількість днів різниці: {result}")
        break
