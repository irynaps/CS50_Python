from datetime import date, datetime
import re
import sys
import inflect


class MinutesCalc:
    def __init__(self, i_date):
        self.i_date = i_date


    def calculate(self):
        i_date = datetime.strptime(self.i_date, '%Y-%m-%d').date()
        t_date = date.today()
        difference = t_date - i_date
        minutes_diff = difference.total_seconds() / 60
        return minutes_diff


def main():
    input_date = input("Date of Birth: ")
    check_date(input_date)
    print(convert_to_mins(input_date))


def convert_to_mins(input_date):
    i_date = MinutesCalc(input_date)
    diff = i_date.calculate()
    p = inflect.engine()
    words = p.number_to_words(int(diff), andword="")
    return (f"{words.capitalize()} minutes")


def check_date(s):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", s):
        year, month, day = s.split("-")
        if int(year) > 2023:
            sys.exit("Invalid date")
        if int(month) > 12:
            sys.exit("Invalid date")
        if int(day) > 31:
            sys.exit("Invalid date")
        if month in ["04", "06", "09", "11"]:
            if int(day) > 30:
                sys.exit("Invalid date")
        if month == "02":
            if int(day) > 29:
                sys.exit("Invalid date")
            if day == "29" and not (int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0)):
                sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()