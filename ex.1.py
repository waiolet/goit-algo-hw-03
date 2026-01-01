from datetime import datetime
current_datetime = datetime.now().date()


def get_days_from_today(date):
    input_date = datetime.fromisoformat(date).date()
    today = datetime.today().date()
    return (input_date - today).days


date = input("Введіть дату у форматі YYYY-MM-DD: ")
print(get_days_from_today(date))