import random

def build_character_pool(allow_alpha, allow_digits, allow_special):
    pool = ""

    if allow_alpha:
        pool += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if allow_digits:
        pool += "0123456789"

    if allow_special:
        pool += "!@#$%^&*()-_=+[]{};:,.<>/?"

    return pool


def create_password(size, pool):
    password_output = ""

    for i in range(size):
        random_index = random.randint(0, len(pool) - 1)
        password_output += pool[random_index]

    return password_output


print("\n====== RANDOM PASSWORD GENERATOR ======\n")

try:
    pwd_length = int(input("Enter required password length: "))

    alpha_choice = input("Allow alphabets? (yes/no): ").strip().lower() == "yes"
    digit_choice = input("Allow numbers? (yes/no): ").strip().lower() == "yes"
    special_choice = input("Allow symbols? (yes/no): ").strip().lower() == "yes"

    character_pool = build_character_pool(alpha_choice, digit_choice, special_choice)

    if character_pool == "":
        print("\nError: No character set selected!")
    else:
        final_password = create_password(pwd_length, character_pool)
        print("\nGenerated Secure Password:", final_password)

except:
    print("\nInvalid input! Please enter numeric value for length.")
