"""LESSON 01.30: return

Run: python course/01_functions/30_return_values.py

`print` displays something for a human. `return` sends a value back to the code
that called the function.

    def add(left, right):
        return left + right

    total = add(2, 3)

After the call, total refers to 5. This makes functions reusable: another part
of the program can store, compare, print, or calculate with the returned value.

When Python reaches return, that function call ends. Code indented below the
return in the same path will not run.
"""


# WORKED EXAMPLE
def add(left, right):
    return left + right


result = add(2, 3)
print(result)
assert result == 5


# YOUR TURN 1
def double(number):
    # TODO: return number multiplied by 2.
    pass


assert double(4) == 8, "double(4) should return 8; did you use return?"
assert double(10) == 20, "Use the number parameter rather than a fixed value"


# YOUR TURN 2
def make_greeting(name):
    # TODO: return "Hello " followed by name.
    # You can join strings with +, such as "A" + "B".
    pass


assert make_greeting("Ada") == "Hello Ada", "Return the greeting string"
assert make_greeting("Lin") == "Hello Lin", "Use the name parameter"
print("Lesson 01.30 passed: your functions return useful values.")
