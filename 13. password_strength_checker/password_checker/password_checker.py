def validate_password_string(password):
    if not isinstance(password, str):
        raise TypeError("The password should be a string.")


def check_length(password):
    return len(password) > 8


def has_lowercase_letters(password):
    return any(letter.islower() for letter in password)


def has_uppercase_letters(password):
    return any(letter.isupper() for letter in password)


def has_digits(password):
    return any(character.isdigit() for character in password)


def has_whitespace(password):
    return any(character.isspace() for character in password)


def has_special_characters(password):
    return any(
        character
        for character in password
        if (
            not has_digits(character)
            and not character.isalpha()
            and not has_whitespace(character)
        )
    )


def password_strength(password):
    validate_password_string(password)

    if not check_length(password):
        return "invalid"

    password_checks = [
        has_lowercase_letters(password),
        has_uppercase_letters(password),
        has_digits(password),
        has_special_characters(password),
        has_whitespace(password),
    ]

    checks_passed = sum(password_checks) + 2

    if checks_passed < 3:
        return "invalid"
    elif checks_passed == 3:
        return "weak"
    elif 3 < checks_passed <= 5:
        return "medium"
    elif checks_passed >= 6:
        return "strong"


print(password_strength(""))