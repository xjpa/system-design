"""LESSON 01.20: Function inputs

Run: python course/01_functions/20_parameters_and_arguments.py

Some recipes need ingredients. Functions receive inputs through PARAMETERS:

    def greet(name):
        print("Hello", name)

`name` is a parameter: a temporary variable used inside the function.

    greet("Ada")

`"Ada"` is an argument: the actual value supplied when calling the function.
During this call, name refers to "Ada".

Multiple inputs are separated with commas:

    def show_total(price, quantity):
        print(price * quantity)

    show_total(10, 3)
"""


# WORKED EXAMPLE
def greet(name):
    print("Hello", name)


greet("Ada")
greet("Lin")


# YOUR TURN 1
def introduce(name, job):
    # TODO: print name and job. Any readable sentence is fine.
    pass


introduce("Sam", "developer")


print("Lesson 01.20 finished. Confirm that Sam's introduction appeared above.")
