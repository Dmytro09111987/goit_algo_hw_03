from datetime import datetime

def get_days_from_today(date: str) -> int:
    matrix_of_date = [
        "%Y %m %d", "%y %m %d", "%Y %B %d", "%y %b %d",
        "%d %m %Y", "%d %m %y", "%d %B %Y", "%d %b %y",
        "%m %d %Y", "%m %d %y", "%m %d %B", "%b %d %y",

        "%Y-%m-%d", "%y-%m-%d", "%Y-%B-%d", "%y-%b-%d",
        "%d-%m-%Y", "%d-%m-%y", "%d-%B-%Y", "%d-%b-%y",
        "%m-%d-%Y", "%m-%d-%y", "%m-%d-%B", "%b-%d-%y",

        "%Y/%m/%d", "%y/%m/%d", "%Y/%B %d", "%y/%b/%d",
        "%d/%m/%Y", "%d/%m/%y", "%d/%B %Y", "%d/%b/%y",
        "%m/%d/%Y", "%m/%d/%y", "%m/%d %B", "%b/%d/%y",
    ]

    for format in matrix_of_date:
        try:
            entry_date = datetime.strptime(date, format).date()
            today = datetime.now().date()
            delta = today - entry_date
            return delta.days
        except ValueError:
            continue
    print("Error: Date mast be in ISO formats")
    return None

result = get_days_from_today("09 10 2025")
print(result)