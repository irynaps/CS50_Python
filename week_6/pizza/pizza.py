import sys
import csv
from tabulate import tabulate

def main():
    check_command_line()
    print(tabulate(make_list(sys.argv[1]), headers="firstrow", tablefmt="grid"))


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")


def make_list(file_name):
    menu = []
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
            return menu
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")


if __name__ == "__main__":
    main()