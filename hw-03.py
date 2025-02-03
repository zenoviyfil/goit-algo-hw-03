from datetime import datetime
import random
import re

def string_to_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

def get_days_from_today(date):
    try:
        today = datetime.today().date()
        target_date = string_to_datetime(date).date()
        delta = (target_date - today).days
        return delta
    except ValueError as error:
        return str(error)

def get_numbers_ticket(min, max, quantity): 
    if min < 1 or max > 1000 or quantity > (max - min - 1):
        return []
    
    ticket_numbers = random.sample(range(min, max), quantity)
    
    return sorted(ticket_numbers)

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    
    if phone_number.startswith('380'):
        return f"+{phone_number}"
    elif phone_number.startswith('0'):
        return f"+380{phone_number[1:]}"
    else:
        return f"+380{phone_number}"
    

def date_to_string(date):
    return date.strftime("%Y.%m.%d")
    
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = datetime.today()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    
    return upcoming_birthdays



print(get_days_from_today("2025-02-02"))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

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

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.02.21"},
    {"name": "John Doe", "birthday": "1985.02.14"},
    {"name": "Jane Smith", "birthday": "1990.02.07"}
]

print(get_upcoming_birthdays(users, days=7))