def main():
    fraction = input("Fraction: ")
    converted_fraction = convert(fraction)
    output = gauge(converted_fraction)
    print(output)


def convert(fraction):
    while True:
        try:
            num, denom = fraction.split("/")
            x = int(num)
            y = int(denom)
            f = x / y
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(round(percentage)) + "%"


if __name__ == "__main__":
    main()