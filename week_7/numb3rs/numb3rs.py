import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        ip_parts = ip.split(".")
        for part in ip_parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()