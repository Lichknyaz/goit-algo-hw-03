def get_days_from_today(date_input):
    try:
        from datetime import datetime
        date_object = datetime.strptime(date_input, "%Y-%m-%d")
        date_difference = datetime.now() - date_object
        return date_difference.days
    except ValueError:
         print("Невірний формат дати")

print(get_days_from_today("2024-1-1"))