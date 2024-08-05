import sys

def main():
    check_command_line()
    row_number = read_file(sys.argv[1])
    print(row_number)


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            count = 0
            for line in file:
                line = line.strip()
                if line and not line.startswith("# "):
                    count +=1
            return count
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")


if __name__ == "__main__":
    main()