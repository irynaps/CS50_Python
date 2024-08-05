def main():
    time = input("What time is it? ")
    decimal_time = convert(time)

    if decimal_time >= 7 and decimal_time <= 8:
        print("breakfast time")
    elif decimal_time >= 12 and decimal_time <= 13:
        print("lunch time")
    elif decimal_time >= 18 and decimal_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes


if __name__ == "__main__":
    main()
