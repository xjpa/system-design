"""FOUNDATIONS 02: What does def mean?

Run: python foundations/02_def_and_functions.py

`def` means DEFINE A FUNCTION.

A function is a named group of instructions. Imagine writing a recipe once and
then using that recipe whenever you need it.

    def say_hello():
        print("Hello!")

Read it piece by piece:

    def             "I am defining a function"
    say_hello       the function's name
    ()              inputs go inside these parentheses; this one has no inputs
    :               the function's indented body starts next
    four spaces     every instruction belonging to the function is indented

Defining the function does NOT run its body. This runs it (calls it):

    say_hello()

The parentheses in a call mean "run this function now".
"""


# WORKED EXAMPLE
def say_hello():
    print("Hello!")


say_hello()  # This is a function CALL.
say_hello()  # A function can be called more than once.


# YOUR TURN 1
# Define a function named cheer. Its body should print "You can do this!"
def cheer():
    # TODO: replace pass with a print(...) instruction.
    # `pass` means "do nothing for now" and keeps unfinished Python valid.
    pass


print("Calling your cheer function:")
cheer()

print("Foundations 02 finished. Confirm that your cheer appeared above.")
