import pytest
from decimal import Decimal
from banking.bank_account import BankAccount


@pytest.fixture
def bank_account():
    return BankAccount(12)


def test_no_interest():
    with pytest.raises(TypeError) as error_message:
        BankAccount()
    assert (
        "BankAccount.__init__() missing 1 required positional argument: 'interest_rate'"
        in str(error_message)
    )


@pytest.mark.parametrize(
    "invalid_interest",
    [
        "11",
        (),
        True,
        False,
        {},
    ],
)
def test_invalid_interest(invalid_interest, bank_account):
    with pytest.raises(
        AssertionError,
        match=f"Only an integer, float, or decimal is allowed: {invalid_interest}",
    ):
        bank_account.interest_rate = invalid_interest


@pytest.mark.parametrize(
    "invalid_balance",
    [
        "1000",
        (),
        True,
        False,
        {},
    ],
)
def test_invalid_balance(invalid_balance, bank_account):
    with pytest.raises(
        AssertionError,
        match=f"Only an integer, float, or decimal is allowed: {invalid_balance}",
    ):
        bank_account.balance = invalid_balance


@pytest.mark.parametrize(
    "negative_interest",
    [
        -10,
        -11,
        -12,
    ],
)
def test_negative_interest(negative_interest, bank_account):
    with pytest.raises(
        AssertionError, match=f"Negative value not allowed: {negative_interest}"
    ):
        bank_account.interest_rate = negative_interest


@pytest.mark.parametrize(
    "negative_balance",
    [
        -1000,
        -1100,
        -1200,
    ],
)
def test_negative_balance(negative_balance, bank_account):
    with pytest.raises(
        AssertionError, match=f"Negative value not allowed: {negative_balance}"
    ):
        bank_account.balance = negative_balance


@pytest.mark.parametrize(
    "invalid_deposit",
    [
        "5000",
        (),
        True,
        False,
        {},
    ],
)
def test_invalid_deposit(invalid_deposit, bank_account):
    with pytest.raises(
        AssertionError,
        match=f"Only an integer, float, or decimal is allowed: {invalid_deposit}",
    ):
        bank_account.deposit(invalid_deposit)


@pytest.mark.parametrize(
    "negative_deposit_amount",
    [
        -100,
        -1100.50,
        -12.50,
    ],
)
def test_negative_deposit(negative_deposit_amount, bank_account):
    with pytest.raises(
        AssertionError, match=f"Negative value not allowed: {negative_deposit_amount}"
    ):
        bank_account.deposit(negative_deposit_amount)


@pytest.mark.parametrize(
    "deposit_amounts, balance",
    [
        ([100, 500, 1000], 1600),
        ([500, 100], 600),
        ([100, 100, 200, 50, 50, 500], 1000),
    ],
)
def test_deposit(deposit_amounts, balance, bank_account):

    for deposit in deposit_amounts:
        bank_account.deposit(deposit)
    assert bank_account.balance == balance


@pytest.mark.parametrize(
    "invalid_withdrawal",
    [
        "50",
        (),
        True,
        False,
        {},
    ],
)
def test_invalid_withdrawal_amount(invalid_withdrawal, bank_account):
    with pytest.raises(
        AssertionError,
        match=f"Only an integer, float, or decimal is allowed: {invalid_withdrawal}",
    ):
        bank_account.withdraw(invalid_withdrawal)


@pytest.mark.parametrize(
    "negative_withdrawal_amount",
    [
        -50,
        -500,
        -2,
    ],
)
def test_negative_withdrawals(negative_withdrawal_amount, bank_account):
    with pytest.raises(
        AssertionError,
        match=f"Negative value not allowed: {negative_withdrawal_amount}",
    ):
        bank_account.withdraw(negative_withdrawal_amount)


@pytest.mark.parametrize(
    "excessive_withdrawal_amount",
    [
        500,
        1000,
        20000,
    ],
)
def test_is_balance_sufficient_for_withdrawal(
    excessive_withdrawal_amount, bank_account
):
    with pytest.raises(
        AssertionError,
        match="Withdrawal denied: withdrawal amount exceeds balance amount",
    ):
        bank_account.withdraw(excessive_withdrawal_amount)


@pytest.mark.parametrize(
    "withdrawal_amounts, balance",
    [
        ([500], 99500),
        ([200], 99800),
        ([1000], 99000),
        ([500, 200, 1000], 98300),
    ],
)
def test_withdrawal(withdrawal_amounts, balance, bank_account):
    bank_account.balance = 100000

    for withdrawal in withdrawal_amounts:
        bank_account.withdraw(withdrawal)
    assert bank_account.balance == balance


@pytest.mark.parametrize(
    "months, balance",
    [
        (0, Decimal("1000")),
        (1, Decimal("1010")),
        (2, Decimal("1020.10")),
        (3, Decimal("1030.30")),
        (4, Decimal("1040.60")),
    ],
)
def test_compound_interest(months, balance, bank_account):
    bank_account.balance = 1000

    for month in range(months):
        bank_account.compound_interest()

    assert bank_account.balance == balance
