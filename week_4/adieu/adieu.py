import inflect

p = inflect.engine()
list = []

while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        print("")
        break

p_list = p.join(list)
print("Adieu, adieu, to", p_list)