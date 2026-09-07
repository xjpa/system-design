"""LESSON 03.20: Validation and error-handling pattern drills.

Run: python course/03_errors_and_validation/20_validation_patterns.py

Validation follows a repeatable sequence:

    check boundary input -> raise a precise error -> continue with valid data

Do not catch an exception unless this layer can recover from it or translate it.
"""


# WORKED EXAMPLE — reject invalid input before doing useful work
def require_non_blank(text):
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("text cannot be blank")
    return cleaned


def expect_error(error_type, action):
    try:
        action()
    except error_type:
        return
    raise AssertionError("Expected " + error_type.__name__)


assert require_non_blank("  ready  ") == "ready"


# PATTERN 1 — guard clause for one invalid value
def require_positive(number):
    # TODO: raise ValueError when number is zero or negative; otherwise return it.
    pass


assert require_positive(4) == 4
expect_error(ValueError, lambda: require_positive(0))


# PATTERN 2 — normalize before checking
def clean_title(title):
    # TODO: strip surrounding whitespace into a new local variable.
    # TODO: raise ValueError if that result is blank, otherwise return it.
    pass


assert clean_title("  Fix API  ") == "Fix API"
expect_error(ValueError, lambda: clean_title("   "))


# PATTERN 3 — distinguish bad types from bad values
def percentage(value):
    # TODO: raise TypeError unless value is an int or float.
    # TODO: raise ValueError unless value is between 0 and 100 inclusive.
    # TODO: return value divided by 100.
    pass


assert percentage(25) == 0.25
expect_error(TypeError, lambda: percentage("25"))
expect_error(ValueError, lambda: percentage(120))


# PATTERN 4 — translate a low-level error at a boundary
def parse_quantity(text):
    try:
        # TODO: convert text with int(...) and store the result.
        quantity = None
    except ValueError as error:
        raise ValueError("quantity must be a whole number") from error
    # TODO: use require_positive to validate the converted result.
    pass


assert parse_quantity("3") == 3
expect_error(ValueError, lambda: parse_quantity("three"))
expect_error(ValueError, lambda: parse_quantity("-2"))


# TRANSFER CHALLENGE — validate each stage of a small input pipeline
def parse_port(text):
    """Return an integer port in the inclusive range 1..65535."""
    # TODO: translate non-integer input into ValueError("port must be a number").
    # TODO: raise ValueError("port out of range") for an invalid number.
    pass


assert parse_port("8080") == 8080
expect_error(ValueError, lambda: parse_port("http"))
expect_error(ValueError, lambda: parse_port("70000"))

print("Lesson 03.20 passed: invalid input is rejected at clear boundaries.")
