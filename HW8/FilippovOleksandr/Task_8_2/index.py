import re

def prompt_for_valid_password():
    """
    Повертає дійсний пароль, що задовольняє умови:
      - Мінімум одна маленька літера (a-z)
      - Мінімум одна велика літера (A-Z)
      - Мінімум одна цифра (0-9)
      - Мінімум один зі спеціальних символів: $, #, @
      - Довжина від 6 до 16 символів
    Запитує пароль у користувача, поки не буде введено вірний.
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$"

    while True:
        password = input("Enter your password: ").strip()

        if re.fullmatch(pattern, password):
            print("PasYou have successfully set your password. Terminating program.")
            return True
        else:
            print("Password is invalid. It must meet the following criteria:")
            print("- At least one lowercase letter (a-z)")
            print("- At least one uppercase letter (A-Z)")
            print("- At least one digit (0-9)")
            print("- At least one special character ($, #, @)")
            print("- Length between 6 and 16 characters.")

prompt_for_valid_password()
