import pytest
from validate_sa_id.validate_sa_id import (
    is_id_number_valid,
    has_valid_dob,
    has_valid_citizen_status,
    has_valid_checksum,
)


@pytest.mark.parametrize(
    "dob_validation_id, boolean",
    [
        ("0001300000005", True),
        ("0001-15000000", False),
        ("0001120000003", True),
        ("0001320000001", False),
        ("0001000000008", False),
        ("0001310000003", True),
        ("2001010000004", True),
        ("2401010000006", True),
        ("-120101000000", False),
        ("+980101000000", False),
        ("0.50101000000", False),
        ("0020010000006", False),
        ("00-12000000000", False),
        ("0012010000003", True),
        ("0001010000006", True),
        ("0000010000008", False),
    ],
)
def test_has_valid_dob(dob_validation_id, boolean):
    assert has_valid_dob(dob_validation_id) is boolean


@pytest.mark.parametrize(
    "citizenship_validation_id, boolean",
    [
        ("0001010000006", True),
        ("0001016000109", True),
        ("0002014000208", False),
        ("0001010100509", False),
        ("0001019000206", False),
    ],
)
def test_has_valid_citizen_status(citizenship_validation_id, boolean):
    assert has_valid_citizen_status(citizenship_validation_id) is boolean


@pytest.mark.parametrize(
    "checksum_validation_id, boolean",
    [
        ("0010100000008", True),
        ("9801015000104", True),
        ("0201014000000", False),
        ("0010100100101", False),
        ("0001019000000", False),
    ],
)
def test_has_valid_checksum(checksum_validation_id, boolean):
    assert has_valid_checksum(checksum_validation_id) is boolean


@pytest.mark.parametrize(
    "length_validation_id, boolean",
    [
        ("2001014800086", True),
        ("2309035800088", True),
        ("123", False),
        ("123456789987456123", False),
    ],
)
def test_is_id_number_length_valid(length_validation_id, boolean):
    assert is_id_number_valid(length_validation_id) is boolean


@pytest.mark.parametrize(
    "numeric_validation_id, boolean",
    [
        ("2001014800086", True),
        ("2309035800088", True),
        ("20010A4800086", False),
        ("YY00000000000", False),
        ("00MM000000000", False),
        ("0000DD0000000", False),
    ],
)
def test_is_id_number_numeric(numeric_validation_id, boolean):
    assert is_id_number_valid(numeric_validation_id) is boolean


@pytest.mark.parametrize(
    "id_invalid_dob, boolean",
    [
        ("0000010000008", False),
        ("0001320000001", False),
        ("0001330000009", False),
        ("9999990000006", False),
    ],
)
def test_is_id_number_invalid_dob(id_invalid_dob, boolean):
    assert is_id_number_valid(id_invalid_dob) is boolean


@pytest.mark.parametrize(
    "id_invalid_citizen_status, boolean",
    [
        ("0002014000208", False),
        ("0001010100509", False),
        ("0001019000206", False),
    ],
)
def test_is_id_number_invalid_citizen_status(id_invalid_citizen_status, boolean):
    assert is_id_number_valid(id_invalid_citizen_status) is boolean


@pytest.mark.parametrize(
    "id_invalid_checksum, boolean",
    [
        ("0201014000000", False),
        ("0010100100101", False),
        ("0001019000000", False),
    ],
)
def test_is_id_number_invalid_checksum(id_invalid_checksum, boolean):
    assert is_id_number_valid(id_invalid_checksum) is boolean
