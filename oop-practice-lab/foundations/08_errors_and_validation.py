"""FOUNDATIONS 08: Errors and validation

Run: python foundations/08_errors_and_validation.py

An exception says a function cannot finish normally. Raise one when an input is
invalid instead of returning a misleading answer:

    def divide(total, count):
        if count == 0:
            raise ValueError("count cannot be zero")
        return total / count

`try` attempts code. `except` handles a particular error. In application code,
only catch an error when you can do something useful with it.
"""


# WORKED EXAMPLE
def divide(total, count):
    if count == 0:
        raise ValueError("count cannot be zero")
    return total / count


assert divide(10, 2) == 5
try:
    divide(10, 0)
except ValueError:
    print("The worked example correctly rejected zero.")


# YOUR TURN
def withdraw(balance, amount):
    # TODO: raise ValueError if amount is zero or negative.
    # TODO: raise ValueError if amount is greater than balance.
    # Otherwise return the new balance.
    pass


def expect_value_error(balance, amount):
    try:
        withdraw(balance, amount)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


assert withdraw(100, 30) == 70, "A valid withdrawal should return balance - amount"
expect_value_error(100, 0)
expect_value_error(100, -5)
expect_value_error(100, 101)
print("Foundations 08 passed: your function rejects invalid inputs.")
