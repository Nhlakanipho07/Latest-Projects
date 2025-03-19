import re


def validate_string(string_numbers):
    if not isinstance(string_numbers, str):
        raise TypeError("The input must be a string")


def get_delimiter(string_numbers):
    if re.search(r"//.*\n", string_numbers):
        return re.findall(r"//(.*)\n", string_numbers)[0]


def retrieve_after_newline(string_numbers):
    if re.search(r"\n(.*)", string_numbers):
        return re.findall(r"\n(.*)", string_numbers)[0]


def split_characters(string_numbers):
    delimiter = get_delimiter(string_numbers)

    if retrieve_after_newline(string_numbers) and delimiter:
        characters = retrieve_after_newline(string_numbers).replace(
            delimiter, f",{delimiter},"
        )
        return [char for char in characters.split(",") if char]


def get_all_numbers(string_numbers):
    return re.findall(r"-?\d+", string_numbers)


def get_numbers_adjacent_delimiter(string_numbers):
    return get_all_numbers(string_numbers)[1].split(get_all_numbers(string_numbers)[0])


def validate_delimiter(string_numbers):
    numbers_and_delimiters = split_characters(string_numbers)
    delimiter = get_delimiter(string_numbers)

    if delimiter and numbers_and_delimiters:

        for index, character in enumerate(numbers_and_delimiters[:-1]):
            if (
                character == delimiter
                and numbers_and_delimiters[index + 1] == delimiter
            ):
                raise ValueError(f"Adjacent delimiters are not allowed")

        if (
            numbers_and_delimiters[0] == delimiter
            and numbers_and_delimiters[-1] != delimiter
        ):
            raise ValueError(
                "Delimiter not allowed at the start of the list of integers"
            )
        elif (
            numbers_and_delimiters[-1] == delimiter
            and numbers_and_delimiters[0] != delimiter
        ):
            raise ValueError("Delimiter not allowed at the end of the list of integers")

        elif (
            numbers_and_delimiters[0] == delimiter
            and numbers_and_delimiters[-1] == delimiter
        ):
            raise ValueError(
                "Delimiter not allowed at the start and end of the list of integers"
            )
        elif delimiter in numbers_and_delimiters[1:-1] and delimiter.isdigit():
            for number in get_numbers_adjacent_delimiter(string_numbers):
                for digit in number:
                    if digit in delimiter:
                        raise ValueError(
                            "Integer delimiter not allowed next to the digit being added"
                        )


def reject_negative_numbers(string_numbers):
    negative_numbers = [
        number for number in get_all_numbers(string_numbers) if int(number) < 0
    ]

    if negative_numbers:
        raise ValueError(f"negatives not allowed {','.join(negative_numbers)}")


def add(string_numbers):
    validate_string(string_numbers)
    validate_delimiter(string_numbers)
    reject_negative_numbers(string_numbers)

    if (
        get_delimiter(string_numbers)
        and get_delimiter(string_numbers).isdigit()
        and retrieve_after_newline(string_numbers)
    ):
        return sum(
            int(number) for number in get_numbers_adjacent_delimiter(string_numbers)
        )
    else:
        return sum(int(number) for number in get_all_numbers(string_numbers))
