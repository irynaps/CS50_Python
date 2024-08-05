while True:
    fuel = input("Fraction: ")

    try:
        num, denom = fuel.split("/")
        x = int(num)
        y = int(denom)
        fraction = x / y
        if fraction <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

percentage = fraction * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")