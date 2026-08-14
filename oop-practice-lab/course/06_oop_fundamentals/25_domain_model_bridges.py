"""LESSON 06.25: Small domain-model bridges.

Run: python course/06_oop_fundamentals/25_domain_model_bridges.py

These models are deliberately smaller than Issue. Each drill practices one
domain pattern: protect an invariant, model a state transition, and compose
objects. Keep changes behind methods so invalid states are difficult to create.
"""

from dataclasses import dataclass
from enum import Enum, auto


# WORKED EXAMPLE — the object protects its invariant on every change
class SeatCounter:
    def __init__(self, available: int) -> None:
        if available < 0:
            raise ValueError("available cannot be negative")
        self._available = available

    @property
    def available(self) -> int:
        return self._available

    def reserve_one(self) -> None:
        if self._available == 0:
            raise ValueError("no seats available")
        self._available -= 1


example_seats = SeatCounter(2)
example_seats.reserve_one()
assert example_seats.available == 1


def expect_error(error_type, action):
    try:
        action()
    except error_type:
        return
    raise AssertionError("Expected " + error_type.__name__)


# PATTERN 1 — an invariant remains true after every public operation
class InventoryItem:
    def __init__(self, sku: str, quantity: int = 0) -> None:
        # TODO: reject blank SKUs and negative quantities, then store both.
        raise NotImplementedError

    @property
    def quantity(self) -> int:
        # TODO: expose the private quantity without adding a setter.
        raise NotImplementedError

    def receive(self, amount: int) -> None:
        # TODO: require a positive amount, then increase quantity.
        raise NotImplementedError

    def reserve(self, amount: int) -> None:
        # TODO: require a positive amount no greater than quantity, then subtract.
        raise NotImplementedError


stock = InventoryItem("KEY-1", 2)
stock.receive(3)
stock.reserve(4)
assert stock.quantity == 1
expect_error(ValueError, lambda: stock.reserve(2))


# PATTERN 2 — explicit states and controlled transitions
class LoanStatus(Enum):
    AVAILABLE = auto()
    BORROWED = auto()


class LibraryBook:
    def __init__(self, title: str) -> None:
        self.title = title
        self.status = LoanStatus.AVAILABLE
        self.borrower: str | None = None

    def borrow(self, borrower: str) -> None:
        # TODO: allow this only while AVAILABLE and reject a blank borrower.
        # TODO: store the borrower and change status to BORROWED.
        raise NotImplementedError

    def return_book(self) -> None:
        # TODO: allow this only while BORROWED.
        # TODO: clear the borrower and change status to AVAILABLE.
        raise NotImplementedError


book = LibraryBook("Domain-Driven Design")
book.borrow("Ada")
assert book.status is LoanStatus.BORROWED
assert book.borrower == "Ada"
expect_error(ValueError, lambda: book.borrow("Lin"))
book.return_book()
assert book.status is LoanStatus.AVAILABLE
assert book.borrower is None


# PATTERN 3 — compose small value objects inside an entity
@dataclass(frozen=True)
class OrderLine:
    product: str
    unit_price: int
    quantity: int

    def __post_init__(self) -> None:
        # TODO: reject blank products and non-positive price or quantity.
        pass

    @property
    def subtotal(self) -> int:
        # TODO: return unit_price multiplied by quantity.
        raise NotImplementedError


class ShoppingOrder:
    def __init__(self, order_id: int) -> None:
        self.id = order_id
        self._lines: list[OrderLine] = []

    @property
    def lines(self) -> tuple[OrderLine, ...]:
        # TODO: return an immutable tuple view of the lines.
        raise NotImplementedError

    def add_line(self, line: OrderLine) -> None:
        # TODO: append the already-valid value object.
        raise NotImplementedError

    @property
    def total(self) -> int:
        # TODO: accumulate every line's subtotal.
        raise NotImplementedError


order = ShoppingOrder(42)
order.add_line(OrderLine("Keyboard", 50, 2))
order.add_line(OrderLine("Mouse", 25, 1))
assert order.total == 125
assert order.lines == (
    OrderLine("Keyboard", 50, 2),
    OrderLine("Mouse", 25, 1),
)
expect_error(ValueError, lambda: OrderLine("Monitor", 100, 0))

print("Lesson 06.25 passed: invariants, transitions, and composition.")
