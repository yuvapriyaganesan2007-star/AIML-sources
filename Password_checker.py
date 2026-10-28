while True:
    print("\n===== PASSWORD CHECKER =====")
    print("1. Check Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter your password: ")

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for character in password:
            if character.isupper():
                has_upper = True
            elif character.islower():
                has_lower = True
            elif character.isdigit():
                has_digit = True
            else:
                has_special = True

        if len(password) < 8:
            print("Password must contain at least 8 characters.")
        else:
            print("Password length: Valid")

        print("Contains uppercase letter:", has_upper)
        print("Contains lowercase letter:", has_lower)
        print("Contains number:", has_digit)
        print("Contains special character:", has_special)

        if (len(password) >= 8 and has_upper
                and has_lower and has_digit and has_special):
            print("\nPassword Strength: Strong")
        elif len(password) >= 8 and (has_upper or has_lower) and has_digit:
            print("\nPassword Strength: Moderate")
        else:
            print("\nPassword Strength: Weak")

    elif choice == "2":
        print("Thank you for using Password Checker!")
        break

    else:
        print("Invalid choice. Please try again.")
```
