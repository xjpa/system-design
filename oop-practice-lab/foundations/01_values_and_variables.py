"""FOUNDATIONS 01: Values and variables

Run: python foundations/01_values_and_variables.py

A VALUE is a piece of data:

    "Ada"       text, called a string or str
    25          a whole number, called an integer or int
    True        a yes/no value, called a boolean or bool

A VARIABLE is a name that refers to a value:

    student_name = "Ada"

Read = here as "gets the value", not "is mathematically equal to".
The variable student_name gets the value "Ada".

Python names are case-sensitive: age and Age are different names.
"""

# WORKED EXAMPLE
product_name = "Keyboard"
price = 50
in_stock = True

print(product_name)
print(price)
print(in_stock)

# YOUR TURN
# Replace the three ??? values. Keep quotation marks around text.
learner_name = "???"
hours_practiced = -1
enjoys_python = False

# CHECKS
assert learner_name != "???", "Replace ??? with your name"
assert hours_practiced >= 0, "Use zero or a positive whole number"
assert enjoys_python is True or enjoys_python is False

print("Foundations 01 passed: you created and used variables.")
