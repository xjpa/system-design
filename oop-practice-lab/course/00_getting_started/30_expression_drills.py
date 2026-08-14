"""LESSON 00.30: Values, variables, and expression micro-drills.

Run: python course/00_getting_started/30_expression_drills.py

Complete one TODO at a time. Before running the file, predict the value and
type of the expression you wrote. These drills build the pattern:

    input values -> expression -> named result
"""


# WORKED EXAMPLE — two inputs become one named result
unit_price = 7
units = 2
example_total = unit_price * units
assert example_total == 14


# DRILL 1 — arithmetic: calculate before assigning
item_price = 12
item_count = 3
# TODO: replace None with item_price multiplied by item_count.
subtotal = None
assert subtotal == 36


# DRILL 2 — reuse an earlier result instead of repeating the calculation
shipping_fee = 5
# TODO: calculate subtotal plus shipping_fee.
order_total = None
assert order_total == 41


# DRILL 3 — strings: build a value from smaller pieces
first_name = "Ada"
last_name = "Lovelace"
# TODO: join the names with one space between them.
full_name = None
assert full_name == "Ada Lovelace"


# DRILL 4 — booleans: comparisons themselves produce True or False
minimum_age = 18
customer_age = 21
# TODO: use >= to record whether the customer is old enough.
is_old_enough = None
assert is_old_enough is True


# DRILL 5 — combine two facts with `and`
has_ticket = True
# TODO: the customer may enter only if both facts are true.
may_enter = None
assert may_enter is True


# TRANSFER CHALLENGE — decompose a bill into named intermediate results
meal_price = 80
tip_rate = 0.20
# TODO: calculate tip_amount, then final_bill using tip_amount.
tip_amount = None
final_bill = None
assert tip_amount == 16
assert final_bill == 96

print("Lesson 00.30 passed: expressions turn inputs into named results.")
