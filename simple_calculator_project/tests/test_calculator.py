from simple_calculator import calculator
import pytest


def test_for_when_an_error_is_raised_for_invalid_inputs():
    with pytest.raises(TypeError, match="Please enter integers only."):
        calculator.multiply(1, 2, "three", 4, 5, "6")
    with pytest.raises(TypeError, match="Please enter integers only."):
        calculator.add("1", 2, 3, "5", "six")


@pytest.mark.parametrize(
    "integers, result",
    [
        ((), 0),
        ((1, 2), 3),
        ((-1, -1), -2),
        ((4, -1), 3),
        ((1, 2, 3, 4, 5), 15),
    ],
)
def test_add(integers, result):
    assert calculator.add(*integers) == result


@pytest.mark.parametrize(
    "integers, result",
    [
        ((), 1),
        ((1, 3), 3),
        ((-1, -3), 3),
        ((-1, 3), -3),
        ((1, 2, 3, 4, 5), 120),
    ],
)
def test_multiply(integers, result):
    assert calculator.multiply(*integers) == result
