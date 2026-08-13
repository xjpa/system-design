"""Milestone 0: Your first useful class.

Run this file directly:

    python exercises/00_bank_account.py

Your task is to implement BankAccount until every assertion at the bottom
passes. Work only in this file.

Concepts: class, object, __init__, attributes, methods, validation, exceptions.
"""


class BankAccount:
    """A bank account that owns its balance and protects it from invalid changes."""

    def __init__(self, owner: str) -> None:
        # TODO: Reject a blank owner and start the balance at zero.
        raise NotImplementedError

    @property
    def owner(self) -> str:
        raise NotImplementedError

    @property
    def balance(self) -> int:
        raise NotImplementedError

    def deposit(self, amount: int) -> None:
        """Add a positive whole-number amount."""
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        """Remove a positive amount, but never overdraw the account."""
        raise NotImplementedError


def check_raises(error_type: type[Exception], action: object) -> None:
    """Tiny test helper; you do not need to edit or fully understand it yet."""
    try:
        action()  # type: ignore[operator]
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}")


def run_tests() -> None:
    account = BankAccount("Ada")
    assert account.owner == "Ada"
    assert account.balance == 0

    account.deposit(100)
    account.withdraw(35)
    assert account.balance == 65

    check_raises(ValueError, lambda: BankAccount("  "))
    check_raises(ValueError, lambda: account.deposit(0))
    check_raises(ValueError, lambda: account.deposit(-1))
    check_raises(ValueError, lambda: account.withdraw(0))
    check_raises(ValueError, lambda: account.withdraw(1000))
    assert account.balance == 65

    print("Milestone 0 passed: BankAccount protects its own state.")


if __name__ == "__main__":
    run_tests()
