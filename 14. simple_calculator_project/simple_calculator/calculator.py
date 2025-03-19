def integer_validator(*integers):

    for integer in integers:
        if not isinstance(integer, int):
            raise TypeError("Please enter integers only.")


def add(*integers):
    integer_validator(*integers)
    result = 0

    for number in integers:
        result += number
    return result


def multiply(*integers):
    integer_validator(*integers)
    result = 1

    for number in integers:
        result *= number
    return result
