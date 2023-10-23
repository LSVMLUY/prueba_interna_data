def print_full_name(first, last):
    full_name = f"{first} {last}"
    return full_name

if __name__ == '__main__':  ##esto se ejecuta solo cuando se ejecuta directamente este modulo (no desde IDE)
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = print_full_name(first_name, last_name)
    print("Full Name:", full_name)
