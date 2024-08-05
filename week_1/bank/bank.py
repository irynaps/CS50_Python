input = input("Greeting: ").casefold().split()

first_word = input[0].replace(",", "")
first_char = input[0].casefold()

if first_word == "hello":
    print("$0")
elif first_word == "hey":
    print("$20")
elif first_char[0] == "h":
    print("$20")
else:
    print("$100")