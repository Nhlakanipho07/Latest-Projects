from datetime import datetime


def has_valid_dob(id_string) -> bool:
    try:
        datetime.strptime(id_string[:6], "%y%m%d")
        return True
    except ValueError:
        return False


def has_valid_citizen_status(id_string):
    if len(id_string) == 13:
        return 0 <= int(id_string[10:11]) <= 1


def has_valid_checksum(id_string):
    if id_string.isdigit():
        list_id_digits = ",".join(id_string[:-1]).split(",")
        list_id_digits.reverse()
        list_results = []

        for id_index, id_digit in enumerate(list_id_digits):
            if id_index % 2 == 0:
                if int(id_digit) * 2 > 9:
                    list_results.append(int(id_digit) * 2 - 9)
                else:
                    list_results.append(int(id_digit) * 2)
            else:
                list_results.append(int(id_digit))

        return 10 - sum(list_results) % 10 == int(id_string[-1])
    else:
        return False


def is_id_number_valid(id_string):
    return all(
        (
            id_string.isdigit(),
            len(id_string) == 13,
            has_valid_dob(id_string),
            has_valid_citizen_status(id_string),
            has_valid_checksum(id_string),
        )
    )
