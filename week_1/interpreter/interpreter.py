input = input("Expression: ").split(" ")

first_num = float(input[0])
second_num = float(input[2])
sign = input[1]

match sign:
    case "+":
        print(first_num + second_num)
    case "-":
        print(first_num - second_num)
    case "*":
        print(first_num * second_num)
    case "/":
        print(first_num / second_num)