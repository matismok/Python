def is_leap(year_input):
    if year_input % 4 == 0:
        if year_input % 100 == 0:
            if year_input % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_input, month_input):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_input > 12 or month_input < 1:
        return "Invalid month"
    if month_input == 2:
        if is_leap(year_input):
            return month_days[month_input - 1] + 1
        else:
            return month_days[month_input - 1]
    else:
        return month_days[month_input - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"{days} days")

