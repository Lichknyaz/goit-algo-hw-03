users = [
        {"name": "John Doe", "birthday": "1985.05.19"},
    {"name": "Jane Smith", "birthday": "1990.04.13"},
    {"name": "Pope Rock", "birthday": "1990.04.15"}
]

def get_upcoming_birthdays (users):
    upcoming_birthdays_list = []
    for user in users:
        from datetime import datetime, timedelta
        birthday_object = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = datetime(year = datetime.now().year, \
                            month = birthday_object.month, \
                            day = birthday_object.day)
        days_till_birthday = birthday.toordinal() - datetime.now().toordinal()
        if days_till_birthday < 0:
            # Check next year
            pass
        elif days_till_birthday <=7:
            # Have birthday, check weekday
            if birthday.weekday() == 5:
                # Shift to monday from saturday
                congratulation_date = birthday + timedelta (days=2)
                upcoming_birthdays_list.append ({"name" : user.get("name"), "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
            elif birthday.weekday() == 6:
                # Shift to monday from sunday
                congratulation_date = birthday + timedelta (days=1)
                upcoming_birthdays_list.append ({"name" : user.get("name"), "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
            else:
                # No shift
                upcoming_birthdays_list.append ({"name" : user.get("name"), "congratulation_date": birthday.strftime("%Y.%m.%d")})
    return upcoming_birthdays_list
            

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
