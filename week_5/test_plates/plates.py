def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[0].isalpha() and s[1].isalpha():
        return False
    elif len(s) < 2 or len(s) > 6:
        return False

    for i in s:
        if i == "." or i == " " or i == "?" or i == "!":
            return False

    numbers = ""

    for i in s:
        if i.isdigit():
            if s[len(s) - 1].isalpha() or s[len(s) - 2].isalpha():
                return False
            numbers += i

    if not numbers == "":
        if numbers[0] == "0":
            return False

    return True


if __name__ == "__main__":
    main()