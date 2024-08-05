import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        num_one = generate_integer(level)
        num_two = generate_integer(level)
        print(num_one, "+", num_two, "= ", end="")
        for j in range(3):
            try:
                answer = int(input())
                if answer == num_one + num_two:
                    score += 1
                    break
                else:
                    print("EEE")
                    if not j == 2:
                        print(num_one, "+", num_two, "= ", end="")
                    elif j == 2:
                        print(num_one, "+", num_two, "=", (num_one + num_two))
                    pass
            except ValueError:
                print("EEE")
                if not j == 2:
                    print(num_one, "+", num_two, "= ", end="")
                elif j == 2:
                    print(num_one, "+", num_two, "=", (num_one + num_two))
                pass

    print("Score:", score)


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl == 1 or lvl == 2 or lvl == 3:
                break
        except ValueError:
            pass
    return lvl


def generate_integer(level):
    if level == 1:
        int = random.randint(0, 9)
    elif level == 2:
        int = random.randint(10, 99)
    elif level == 3:
        int = random.randint(100, 999)
    return int


if __name__ == "__main__":
    main()