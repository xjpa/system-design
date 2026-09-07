"""LESSON 07.10: Polymorphism with the Strategy pattern.

Run: python course/07_oop_patterns/10_strategy.py

Implement the three policies. Then add WeekendPolicy and one assertion for it.
Concepts: inheritance, abstract methods, polymorphism, Open/Closed Principle.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from enum import Enum, auto


class Priority(Enum):
    NORMAL = auto()
    HIGH = auto()


class ResponsePolicy(ABC):
    @abstractmethod
    def deadline(self, *, opened_at: datetime, priority: Priority) -> datetime:
        pass


class CommunityPolicy(ResponsePolicy):
    """72 hours for either priority."""

    def deadline(self, *, opened_at: datetime, priority: Priority) -> datetime:
        raise NotImplementedError


class BusinessPolicy(ResponsePolicy):
    """24 hours normally; 4 hours for high priority."""

    def deadline(self, *, opened_at: datetime, priority: Priority) -> datetime:
        raise NotImplementedError


class EnterprisePolicy(ResponsePolicy):
    """4 hours normally; 1 hour for high priority."""

    def deadline(self, *, opened_at: datetime, priority: Priority) -> datetime:
        raise NotImplementedError


def run_tests() -> None:
    opened = datetime(2026, 1, 1, 12, tzinfo=timezone.utc)
    examples = [
        (CommunityPolicy(), Priority.NORMAL, 72),
        (CommunityPolicy(), Priority.HIGH, 72),
        (BusinessPolicy(), Priority.NORMAL, 24),
        (BusinessPolicy(), Priority.HIGH, 4),
        (EnterprisePolicy(), Priority.NORMAL, 4),
        (EnterprisePolicy(), Priority.HIGH, 1),
    ]
    for policy, priority, hours in examples:
        actual = policy.deadline(opened_at=opened, priority=priority)
        assert actual == opened + timedelta(hours=hours)
    print("Lesson 07.10 passed: interchangeable policies calculate deadlines.")


if __name__ == "__main__":
    run_tests()
