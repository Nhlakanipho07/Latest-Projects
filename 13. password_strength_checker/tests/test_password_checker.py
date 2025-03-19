import pytest
from password_checker.password_checker import (
    validate_password_string,
    check_length,
    has_lowercase_letters,
    has_uppercase_letters,
    has_digits,
    has_special_characters,
    has_whitespace,
    password_strength,
)


@pytest.mark.parametrize(
    "invalid_password",
    [
        122,
        45.6,
        None,
        (),
        {},
        False,
    ],
)
def test_validate_string(invalid_password):
    with pytest.raises(TypeError, match="The password should be a string."):
        validate_password_string(invalid_password)


@pytest.mark.parametrize(
    "password_length_check, boolean",
    [
        ("iloveu", False),
        ("xxxxxxxxx", True),
        ("notluvyou", True),
        ("loozar", False),
    ],
)
def test_check_length(password_length_check, boolean):
    assert check_length(password_length_check) is boolean


@pytest.mark.parametrize(
    "password_lowercase_check, boolean",
    [
        ("LLLL@##LLLLL", False),
        ("III!!IIIIII", False),
        ("AAAAAAa", True),
        ("rrRRRRrrr", True),
    ],
)
def test_has_lowercase_letters(password_lowercase_check, boolean):
    assert has_lowercase_letters(password_lowercase_check) is boolean


@pytest.mark.parametrize(
    "password_uppercase_check, boolean",
    [
        ("LLLL@##LLLLL", True),
        ("III!!IIIIII", True),
        ("a", False),
        ("rr$%%\\//rrr", False),
    ],
)
def test_has_uppercase_letters(password_uppercase_check, boolean):
    assert has_uppercase_letters(password_uppercase_check) is boolean


@pytest.mark.parametrize(
    "password_digit_check, boolean",
    [
        ("xco2xco3", True),
        ("abcdefg", False),
        ("1", True),
        ("XYZ", False),
    ],
)
def test_has_digits(password_digit_check, boolean):
    assert has_digits(password_digit_check) is boolean


@pytest.mark.parametrize(
    "password_special_characters, boolean",
    [
        ("xco2xco3", False),
        ("Abc123", False),
        ("rr$%%\\//rrr", True),
        (".com", True),
        (",", True),
    ],
)
def test_has_special_characters(password_special_characters, boolean):
    assert has_special_characters(password_special_characters) is boolean


@pytest.mark.parametrize(
    "password_whitespace_check, boolean",
    [
        ("bl ahbla hhh", True),
        (" ", True),
        ("4Real!", False),
        ("lllccc%4$@*GGG", False),
    ],
)
def test_has_whitespace(password_whitespace_check, boolean):
    assert has_whitespace(password_whitespace_check) is boolean


@pytest.mark.parametrize(
    "password_strength_check, strength",
    [
        ("Ab123 @#cde", "strong"),
        ("@4Real Guy!", "strong"),
        ("lllccc%4$@*ggg", "medium"),
        ("xoXOlXOxo", "medium"),
        ("blahahbla", "weak"),
        ("123456100", "weak"),
        ("weekend", "invalid"),
        ("1", "invalid"),
    ],
)
def test_password_strength(password_strength_check, strength):
    assert password_strength(password_strength_check) == strength
