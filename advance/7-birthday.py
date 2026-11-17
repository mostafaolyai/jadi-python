from datetime import date, datetime


birth_date_text = input().strip()

try:
    birth_date = datetime.strptime(birth_date_text, "%Y/%m/%d").date()
    # strptime accepts some non-zero-padded fields, so enforce the exact format.
    if birth_date.strftime("%Y/%m/%d") != birth_date_text:
        raise ValueError
except ValueError:
    print("WRONG")
else:
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    print(age)
