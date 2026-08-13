"""LESSON 04.20: Class practice before the OOP lab

Run: python course/04_classes_and_objects/20_class_practice.py

This combines functions, conditions, validation, attributes, and methods. Once
it passes, you are ready for course/06_oop_fundamentals/10_bank_account.py.

Approach any class problem in this order:

1. Write down what one object KNOWS (its attributes/data).
2. Write down what one object DOES (its methods/behavior).
3. Identify invalid inputs or states.
4. Implement __init__ so every new object starts valid.
5. Implement one method and check it before adding the next.
"""


class ShoppingCart:
    def __init__(self, owner):
        # TODO: reject a blank owner using ValueError.
        # TODO: store owner and create an empty self.prices list.
        pass

    def add_item(self, price):
        # TODO: reject prices that are zero or negative.
        # TODO: append a valid price to self.prices.
        pass

    def item_count(self):
        # TODO: return the number of prices. Hint: len(self.prices)
        pass

    def total(self):
        answer = 0
        # TODO: use a for loop to add every price to answer.
        return answer


def expect_cart_error(owner):
    try:
        ShoppingCart(owner)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


def expect_item_error(cart, price):
    try:
        cart.add_item(price)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


cart = ShoppingCart("Ada")
assert hasattr(cart, "owner"), "In __init__, store owner on self.owner"
assert hasattr(cart, "prices"), "In __init__, create self.prices as an empty list"
assert cart.owner == "Ada"
assert cart.item_count() == 0
assert cart.total() == 0
cart.add_item(50)
cart.add_item(25)
assert cart.item_count() == 2
assert cart.total() == 75
expect_cart_error(" ")
expect_item_error(cart, 0)
expect_item_error(cart, -10)
print("Lesson 04.20 passed: you are ready for the OOP practice lab!")
