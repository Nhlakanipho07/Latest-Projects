import pytest
from decimal import Decimal
from banking.bank import Bank
from banking.bank_account import BankAccount


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def savings_acc_number(bank):
    bank.add_account_type("Savings", 5)
    return bank.open_bank_account("Savings")


@pytest.fixture
def current_acc_number(bank):
    bank.add_account_type("Current", 2.5)
    return bank.open_bank_account("Current")


@pytest.mark.parametrize("invalid_data_type", [(), True, False, {}])
def test_validate_string(invalid_data_type, bank):
    with pytest.raises(TypeError, match=f"{invalid_data_type} must be a string"):
        bank.validate_string(invalid_data_type)


@pytest.mark.parametrize("non_numeric_acc_number", ["12three45", "#15879"])
def test_validate_account_number_numeric(bank, non_numeric_acc_number):
    with pytest.raises(
        ValueError,
        match=f"Account number: {non_numeric_acc_number}, is not numeric. Ensure that the account number consists of digits only",
    ):
        bank.validate_account_number(non_numeric_acc_number)


@pytest.mark.parametrize("account_number", ["12564", "9876543210123456"])
def test_validate_account_number_length(bank, account_number):
    with pytest.raises(
        ValueError,
        match="Please enter a ten digit account number",
    ):
        bank.validate_account_number(account_number)


def test_validate_account_exists(bank):
    account_number = "1234567890"
    with pytest.raises(
        ValueError, match=f"Account number: {account_number}, does not exist"
    ):
        bank.validate_account_exists(account_number)


@pytest.mark.parametrize(
    "account_type_name, interest_rate", [("Savings", 5), ("Current", 2.5)]
)
def test_add_account_type(bank, account_type_name, interest_rate):
    bank.add_account_type(account_type_name, interest_rate)
    assert list(bank.account_types.keys())[0] == account_type_name
    assert list(bank.account_types.values())[0] == interest_rate


def test_account_type_already_exists(bank):
    account_type_name = "Savings"
    interest_rate = 5
    bank.add_account_type(account_type_name, interest_rate)
    with pytest.raises(ValueError, match=f"{account_type_name} already exists"):
        bank.add_account_type(account_type_name, interest_rate)


def test_add_account(bank):
    account_number = "1234567890"
    account_name = "Savings"
    bank.add_account_type("Savings", 5)
    bank.add_account("1234567890", "Savings")
    assert account_number == list(bank.accounts.keys())[0]
    assert account_name == list(bank.accounts.values())[0]["account_type"]
    assert isinstance(list(bank.accounts.values())[0]["account"], BankAccount)


def test_generate_account_number(bank):
    account_number = bank.generate_account_number()
    assert isinstance(account_number, str)
    assert account_number.isdigit()
    assert len(account_number) == 10


@pytest.mark.parametrize("account_name", ["Savings", "Current"])
def test_open_bank_account(account_name, bank):
    bank.add_account_type(account_name, 5)
    account_number = bank.open_bank_account(account_name)
    assert account_number.isdigit()
    assert len(account_number) == 10


def test_deposit(bank, savings_acc_number, current_acc_number):
    bank.deposit(savings_acc_number, 1500)
    bank.deposit(current_acc_number, 500)
    assert bank.accounts[savings_acc_number]["account"].balance == Decimal("1500")
    assert bank.accounts[current_acc_number]["account"].balance == Decimal("500")


def test_withdraw(bank, savings_acc_number, current_acc_number):
    bank.deposit(savings_acc_number, 1500)
    bank.deposit(current_acc_number, 500)
    bank.withdraw(savings_acc_number, 300)
    bank.withdraw(current_acc_number, 200)
    assert bank.accounts[savings_acc_number]["account"].balance == Decimal("1200")
    assert bank.accounts[current_acc_number]["account"].balance == Decimal("300")


def test_transfer(bank, savings_acc_number, current_acc_number):
    bank.deposit(savings_acc_number, 1500)
    bank.deposit(current_acc_number, 500)
    bank.transfer(current_acc_number, savings_acc_number, 200)
    assert bank.accounts[savings_acc_number]["account"].balance == Decimal("1700")
    assert bank.accounts[current_acc_number]["account"].balance == Decimal("300")


def test_compound_interest(bank, savings_acc_number, current_acc_number):
    bank.deposit(savings_acc_number, 1500)
    bank.deposit(current_acc_number, 500)
    bank.compound_interest()
    assert bank.accounts[savings_acc_number]["account"].balance == Decimal("1506.25")
    assert bank.accounts[current_acc_number]["account"].balance == Decimal("501.04")


def test_get_balance(bank, savings_acc_number, current_acc_number):
    assert bank.get_balance(savings_acc_number) == Decimal("0")
    assert bank.get_balance(current_acc_number) == Decimal("0")

    bank.deposit(savings_acc_number, 1500)
    bank.deposit(current_acc_number, 500)
    assert bank.get_balance(savings_acc_number) == Decimal("1500")
    assert bank.get_balance(current_acc_number) == Decimal("500")


def test_get_interest_rate(bank, savings_acc_number, current_acc_number):
    assert bank.get_interest_rate(savings_acc_number) == 5
    assert bank.get_interest_rate(current_acc_number) == 2.5
