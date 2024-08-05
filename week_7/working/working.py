import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    correct = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M)$", s)
    if correct:
        parts = correct.groups()
        if int(parts[1]) > 12 or int(parts[5]) > 12:
            raise ValueError

        hour_first, min_first = am_pm(parts[0], parts[3])
        hour_second, min_second = am_pm(parts[4], parts[7])

        return (f"{hour_first:02}:{min_first:02} to {hour_second:02}:{min_second:02}")
    else:
        raise ValueError


def am_pm(time, format):
    if ":" in time:
        split = time.split(":")
        hour = int(split[0])
        min = int(split[1])
    else:
        hour = int(time)
        min = 0

    if format == "AM" and hour == 12:
        hour = 0
    if format == "PM" and hour != 12:
        hour = hour + 12

    return hour, min


if __name__ == "__main__":
    main()