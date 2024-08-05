import sys
from PIL import Image, ImageOps

def main():
    check_command_line()
    put_tshirt()


def check_command_line():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    extension_one = sys.argv[1].split(".")
    extension_two = sys.argv[2].split(".")
    if check_extension(extension_one[1]) == False:
        sys.exit("Invalid input")
    if check_extension(extension_two[1]) == False:
        sys.exit("Invalid output")
    if extension_one[1] != extension_two[1]:
        sys.exit("Input and output have different extensions")


def check_extension(file_extension):
    if file_extension in ["jpg", "jpeg", "png"]:
        return True
    return False


def put_tshirt():
    try:
        input = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(input, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


if __name__ == "__main__":
    main()