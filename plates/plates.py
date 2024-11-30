
# submit50 cs50/problems/2022/python/plates
#using string methods like isalpha,isdigit,isalnmueric


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length check
    if not (2 <= len(s) <= 6):
        return False

    # Start with letters
    if not s[:2].isalpha():
        return False

    # No spaces or special characters
    if not s.isalnum():
        return False

    # Numbers must appear at the end
    has_number = False
    for char in s:
        if char.isdigit():
            has_number = True
        elif has_number and char.isalpha():  # If a letter follows a number, it's invalid
            return False

    return True


main()
