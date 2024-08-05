def main():
    user_input = input("Input: ")
    user_output = shorten(user_input)
    print("Output:", user_output)


def shorten(word):
    word_output = ""
    for i in word:
        if not check_letter(i.lower()):
            word_output += i
    return word_output


def check_letter(letter):
    if letter == "a" or letter == "e" or letter == "o" or letter == "i" or letter == "u":
        return True
    else:
        return False


if __name__ == "__main__":
    main()