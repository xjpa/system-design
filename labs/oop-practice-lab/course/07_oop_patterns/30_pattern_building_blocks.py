"""LESSON 07.30: Pattern building blocks.

Run: python course/07_oop_patterns/30_pattern_building_blocks.py

A pattern is a response to a design pressure. These drills start with that
pressure, then ask you to implement the smallest useful abstraction.
"""

from dataclasses import dataclass, field
from typing import Protocol


# WORKED EXAMPLE — the caller delegates a varying calculation
class ShippingRule(Protocol):
    def cost(self, weight: int) -> int: ...


class FlatShipping:
    def cost(self, weight: int) -> int:
        return 5


def shipping_cost(weight: int, rule: ShippingRule) -> int:
    return rule.cost(weight)


assert shipping_cost(10, FlatShipping()) == 5


# PRESSURE 1 — an algorithm must vary without changing the caller (Strategy)
class Discount(Protocol):
    def apply(self, price: int) -> int: ...


class NoDiscount:
    def apply(self, price: int) -> int:
        # TODO: return the unchanged price.
        raise NotImplementedError


class PercentageDiscount:
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def apply(self, price: int) -> int:
        # TODO: subtract this percentage using integer arithmetic.
        raise NotImplementedError


def checkout(price: int, discount: Discount) -> int:
    # TODO: delegate the calculation to discount.
    raise NotImplementedError


assert checkout(100, NoDiscount()) == 100
assert checkout(100, PercentageDiscount(20)) == 80


# PRESSURE 2 — an external interface does not match ours (Adapter)
class LegacySmsClient:
    def send_text(self, phone_number: str, text: str) -> None:
        self.last_message = (phone_number, text)


class Notifier(Protocol):
    def notify(self, recipient: str, message: str) -> None: ...


class SmsNotifier:
    def __init__(self, client: LegacySmsClient) -> None:
        # TODO: store the external client.
        raise NotImplementedError

    def notify(self, recipient: str, message: str) -> None:
        # TODO: adapt notify(...) to the client's send_text(...).
        raise NotImplementedError


sms_client = LegacySmsClient()
SmsNotifier(sms_client).notify("+123", "Issue opened")
assert sms_client.last_message == ("+123", "Issue opened")


# PRESSURE 3 — creation rules need one clear home (Factory)
@dataclass
class Ticket:
    title: str
    priority: str


class TicketFactory:
    def create(self, title: str, *, urgent: bool = False) -> Ticket:
        # TODO: strip and validate the title.
        # TODO: return a Ticket with priority "high" if urgent, else "normal".
        raise NotImplementedError


factory = TicketFactory()
assert factory.create("  Login broken  ") == Ticket("Login broken", "normal")
assert factory.create("Outage", urgent=True).priority == "high"


# PRESSURE 4 — a collaborator has side effects we want to observe (Fake/Spy)
@dataclass
class RecordingNotifier:
    messages: list[tuple[str, str]] = field(default_factory=list)

    def notify(self, recipient: str, message: str) -> None:
        # TODO: record the call as a (recipient, message) tuple.
        raise NotImplementedError


def announce(ticket: Ticket, recipient: str, notifier: Notifier) -> None:
    # TODO: notify the recipient with "Opened: " followed by the title.
    raise NotImplementedError


recorder = RecordingNotifier()
announce(Ticket("API failure", "high"), "team", recorder)
assert recorder.messages == [("team", "Opened: API failure")]


# TRANSFER CHALLENGE — add FixedDiscount(amount) without editing checkout.
class FixedDiscount:
    def __init__(self, amount: int) -> None:
        # TODO: store amount.
        raise NotImplementedError

    def apply(self, price: int) -> int:
        # TODO: subtract amount, but never return less than zero.
        raise NotImplementedError


assert checkout(30, FixedDiscount(10)) == 20
assert checkout(5, FixedDiscount(10)) == 0

print("Lesson 07.30 passed: strategies, adapters, factories, and test doubles.")
