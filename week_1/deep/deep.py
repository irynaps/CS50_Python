question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()

if question == "42":
    print("Yes")
elif question == "forty-two":
    print("Yes")
elif question == "forty two":
    print("Yes")
else:
    print("No")