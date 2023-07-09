def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    any_numbers = False
    for c in s:
        if c.isdigit():
            if c=='0' and not any_numbers:
               return False
            any_numbers = True
        elif c.isalpha():
            if any_numbers:
                return False
        else:
            return False
    return True
main()