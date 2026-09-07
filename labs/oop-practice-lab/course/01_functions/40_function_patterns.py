"""LESSON 01.40: Function pattern drills.

Run: python course/01_functions/40_function_patterns.py

Each drill isolates one reusable function shape. Say the shape aloud before
coding it: "one input, transformed output" or "two inputs, combined output."
"""


# WORKED EXAMPLE — one input, transformed output
def square(number):
    return number * number


assert square(3) == 9


# PATTERN 1 — transform one value
def minutes_to_seconds(minutes):
    # TODO: return the number of seconds.
    pass


assert minutes_to_seconds(2) == 120
assert minutes_to_seconds(5) == 300


# PATTERN 2 — combine two values
def rectangle_area(width, height):
    # TODO: return width multiplied by height.
    pass


assert rectangle_area(4, 3) == 12
assert rectangle_area(2, 8) == 16


# PATTERN 3 — compute, name, then return
def price_with_tax(price, tax_rate):
    # TODO: store the tax in a local variable, then return price plus tax.
    pass


assert price_with_tax(100, 0.10) == 110
assert price_with_tax(50, 0.20) == 60


# PATTERN 4 — one function delegates a detail to another function
def format_name(first, last):
    return first + " " + last


def welcome_message(first, last):
    # TODO: call format_name and return "Welcome, Ada Lovelace!".
    pass


assert welcome_message("Ada", "Lovelace") == "Welcome, Ada Lovelace!"
assert welcome_message("Grace", "Hopper") == "Welcome, Grace Hopper!"


# PATTERN 5 — defaults and keyword arguments
def make_label(text, prefix="INFO"):
    # TODO: return a label such as "[INFO] Ready".
    pass


assert make_label("Ready") == "[INFO] Ready"
assert make_label("Disk full", prefix="ERROR") == "[ERROR] Disk full"


# TRANSFER CHALLENGE — decompose instead of writing one giant expression
def calculate_tip(meal_price, tip_rate):
    # TODO: return the tip amount.
    pass


def calculate_bill(meal_price, tip_rate, people):
    # TODO: call calculate_tip, calculate the total, then return each share.
    pass


assert calculate_bill(80, 0.20, 2) == 48
assert calculate_bill(90, 0.10, 3) == 33

print("Lesson 01.40 passed: you practiced reusable function shapes.")
