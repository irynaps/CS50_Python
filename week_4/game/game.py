import random

while True:
    try:
        num = int(input("Level: "))
        if num > 0:
            break
    except ValueError:
        pass

rand_num = random.randint(1, num)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > rand_num:
            print("Too large!")
        elif guess < rand_num:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
