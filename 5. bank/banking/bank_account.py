from decimal import Decimal, getcontext, ROUND_HALF_UP


class BankAccount:
    getcontext().rounding = ROUND_HALF_UP

    def __init__(self, interest_rate, balance=Decimal("0")):
        self.validate_type(interest_rate)
        self.validate_type(balance)
        self.validate_positive(interest_rate)
        self.validate_positive(balance)

        self._balance = Decimal(balance).quantize(Decimal(".00"))
        self._interest_rate = Decimal(interest_rate) / Decimal("1200")

    @property
    def interest_rate(self):
        return self._interest_rate

    @property
    def balance(self):
        return self._balance

    @interest_rate.setter
    def interest_rate(self, value):
        self.validate_type(value)
        self.validate_positive(value)
        self._interest_rate = value

    @balance.setter
    def balance(self, value):
        self.validate_type(value)
        self.validate_positive(value)
        self._balance = value

    @staticmethod
    def validate_type(value):
        assert isinstance(
            value, (int, float, Decimal)
        ), f"Only an integer, float, or decimal is allowed: {value}"

        assert not isinstance(
            value, bool
        ), f"Only an integer, float, or decimal is allowed: {value}"

    @staticmethod
    def validate_positive(value):
        assert Decimal(value) >= Decimal("0"), f"Negative value not allowed: {value}"

    def deposit(self, deposit_amount):
        BankAccount.validate_type(deposit_amount)
        BankAccount.validate_positive(deposit_amount)

        self._balance += Decimal(deposit_amount).quantize(Decimal(".00"))

    def withdraw(self, withdrawal_amount):
        BankAccount.validate_type(withdrawal_amount)
        BankAccount.validate_positive(withdrawal_amount)

        assert Decimal(withdrawal_amount) <= Decimal(
            self._balance
        ), "Withdrawal denied: withdrawal amount exceeds balance amount"

        self._balance -= Decimal(withdrawal_amount).quantize(Decimal(".00"))

    def compound_interest(self):
        self._balance = (
            Decimal(self._balance) * (Decimal("1") + Decimal(self._interest_rate))
        ).quantize(Decimal(".00"))
