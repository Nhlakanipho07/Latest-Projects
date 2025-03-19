import pytest

from string_calculator.string_calculator import (
    validate_string,
    get_delimiter,
    retrieve_after_newline,
    split_characters,
    validate_delimiter,
    get_all_numbers,
    get_numbers_adjacent_delimiter,
    reject_negative_numbers,
    add,
)


@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        [],
        (),
        True,
        123,
    ],
)
def test_validate_string(invalid_input):
    with pytest.raises(TypeError, match="The input must be a string"):
        validate_string(invalid_input)


@pytest.mark.parametrize(
    "string_characters, delimiter",
    [
        ("//***\n1***2***3", "***"),
        ("//4\n142", "4"),
        ("//;\n1;2", ";"),
    ],
)
def test_get_delimiter(string_characters, delimiter):
    assert get_delimiter(string_characters) == delimiter


@pytest.mark.parametrize(
    "string_characters, characters",
    [
        ("//***\n1***2***3", "1***2***3"),
        ("//;\n1;2", "1;2"),
        ("//4\n142", "142"),
        ("//;\n", ""),
    ],
)
def test_retrieve_after_newline(string_characters, characters):
    assert retrieve_after_newline(string_characters) == characters


@pytest.mark.parametrize(
    "string_characters, numbers_and_delimiters",
    [
        ("//***\n1***2***3", ["1", "***", "2", "***", "3"]),
        ("//;\n1;2", ["1", ";", "2"]),
    ],
)
def test_split_characters(string_characters, numbers_and_delimiters):
    assert split_characters(string_characters) == numbers_and_delimiters


@pytest.mark.parametrize(
    "string_characters, error_message",
    [
        (
            "//***\n***1***2***3",
            "Delimiter not allowed at the start of the list of integers",
        ),
        (
            "//***\n1***2***3***",
            "Delimiter not allowed at the end of the list of integers",
        ),
        (
            "//***\n***1***2***3***",
            "Delimiter not allowed at the start and end of the list of integers",
        ),
        (
            "//M\n5M3MMM3M8",
            "Adjacent delimiters are not allowed",
        ),
        (
            "//U\n5U3UUU3",
            "Adjacent delimiters are not allowed",
        ),
        (
            "//N\n89N6NN92",
            "Adjacent delimiters are not allowed",
        ),
        (
            "//4\n434243",
            "Delimiter not allowed at the start of the list of integers",
        ),
        (
            "//4\n342434",
            "Delimiter not allowed at the end of the list of integers",
        ),
        (
            "//4\n4342434",
            "Delimiter not allowed at the start and end of the list of integers",
        ),
        (
            "//88\n18882",
            "Integer delimiter not allowed next to the digit being added",
        ),
    ],
)
def test_validate_delimiter(string_characters, error_message):
    with pytest.raises(ValueError, match=error_message):
        validate_delimiter(string_characters)


@pytest.mark.parametrize(
    "string_characters, list_numbers",
    [
        ("//;\n1;2", ["1", "2"]),
        ("//4\n142", ["4", "142"]),
        ("123", ["123"]),
        ("1,2,3", ["1", "2", "3"]),
        ("//***\n1***2***3", ["1", "2", "3"]),
    ],
)
def test_get_all_numbers(string_characters, list_numbers):
    assert get_all_numbers(string_characters) == list_numbers


@pytest.mark.parametrize(
    "string_characters, list_numbers",
    [
        ("//4\n142", ["1", "2"]),
        ("//12\n34129", ["34", "9"]),
    ],
)
def test_get_numbers_adjacent_delimiter(string_characters, list_numbers):
    assert get_numbers_adjacent_delimiter(string_characters) == list_numbers


@pytest.mark.parametrize(
    "string_numbers, negative_numbers",
    [
        ("-1,-2,3,4", "-1,-2"),
        ("2,4,-6,-8", "-6,-8"),
        ("0,4,8,-12,-16", "-12,-16"),
    ],
)
def test_reject_negative_numbers(string_numbers, negative_numbers):
    with pytest.raises(ValueError, match=f"negatives not allowed {negative_numbers}"):
        reject_negative_numbers(string_numbers)


@pytest.mark.parametrize(
    "string_numbers, total",
    [
        ("", 0),
        ("1", 1),
        ("123", 123),
        ("1,1", 2),
        ("1,2,3,4", 10),
        ("1\n2,3", 6),
        ("//;\n1;2", 3),
        ("//;\n1", 1),
        ("//;\n", 0),
        ("//4\n142", 3),
        ("//12\n34129", 43),
        ("//***\n1***2***3", 6),
    ],
)
def test_add(string_numbers, total):
    assert add(string_numbers) == total
