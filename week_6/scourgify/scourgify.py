import sys
import csv

def main():
    check_command_line()
    students = change(read_file(sys.argv[1]))
    write_file(students)


def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def read_file(file_name):
    students = []
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
            return students
    except FileNotFoundError:
        sys.exit("Could not read", file_name)


def change(students):
    new_students = []
    for item in students:
        name_divided = item['name'].split(', ')
        last_name = name_divided[0].replace('"', '')
        first_name = name_divided[1].replace('"', '')
        new_item = {'last': last_name, 'first': first_name, 'house': item['house']}
        new_students.append(new_item)
    return new_students


def write_file(students):
    file_name = sys.argv[2]
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()