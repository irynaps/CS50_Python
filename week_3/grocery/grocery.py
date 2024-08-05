grocery = {}

while True:
    try:
        item = input().lower()

        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except KeyError:
        pass
    except EOFError:
        print("")
        break

sorted_grocery = dict(sorted(grocery.items(), key=lambda item: item[0]))

for i in sorted_grocery:
    print(sorted_grocery[i], i.upper())