"""Milestone 5: Dependency injection and an application service.

Run: python exercises/05_service.py

Implement IssueService. Supporting classes are intentionally small so this
exercise stays in one file.
Concepts: composition, dependency injection, orchestration, fakes, side effects.
"""

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Protocol
from uuid import UUID


@dataclass
class Issue:
    id: UUID
    title: str
    opened_at: datetime
    assignee: str | None = None
    comments: list[str] = field(default_factory=list)
    resolved: bool = False

    def claim(self, agent: str) -> None:
        if self.resolved or self.assignee is not None:
            raise ValueError("issue cannot be claimed")
        self.assignee = agent

    def add_comment(self, body: str) -> None:
        if not body.strip():
            raise ValueError("comment body cannot be blank")
        self.comments.append(body)

    def resolve(self) -> None:
        if self.assignee is None or not self.comments:
            raise ValueError("assigned issue with a comment is required")
        self.resolved = True


class Repository(Protocol):
    def add(self, issue: Issue) -> None: ...

    def get(self, issue_id: UUID) -> Issue | None: ...

    def update(self, issue: Issue) -> None: ...


class Notifier(Protocol):
    def issue_opened(self, issue: Issue, deadline: datetime) -> None: ...


class Clock(Protocol):
    def now(self) -> datetime: ...


class IssueService:
    def __init__(
        self,
        *,
        repository: Repository,
        notifier: Notifier,
        clock: Clock,
        id_factory: Callable[[], UUID],
    ) -> None:
        # TODO: store, rather than construct, all four dependencies.
        raise NotImplementedError

    def open_issue(self, title: str) -> Issue:
        # TODO: validate title, construct and save an issue, notify with a
        # 24-hour deadline, and return it.
        raise NotImplementedError

    def claim_issue(self, issue_id: UUID, agent: str) -> Issue:
        # TODO: load via _require_issue, call domain behavior, then update.
        raise NotImplementedError

    def comment_on_issue(self, issue_id: UUID, body: str) -> Issue:
        raise NotImplementedError

    def resolve_issue(self, issue_id: UUID) -> Issue:
        raise NotImplementedError

    def _require_issue(self, issue_id: UUID) -> Issue:
        # TODO: raise LookupError when the repository returns None.
        raise NotImplementedError


class FakeRepository:
    def __init__(self) -> None:
        self.items: dict[UUID, Issue] = {}

    def add(self, issue: Issue) -> None:
        self.items[issue.id] = issue

    def get(self, issue_id: UUID) -> Issue | None:
        return self.items.get(issue_id)

    def update(self, issue: Issue) -> None:
        self.items[issue.id] = issue


@dataclass
class FixedClock:
    value: datetime

    def now(self) -> datetime:
        return self.value


@dataclass
class RecordingNotifier:
    events: list[tuple[Issue, datetime]] = field(default_factory=list)

    def issue_opened(self, issue: Issue, deadline: datetime) -> None:
        self.events.append((issue, deadline))


def expect_error(error_type: type[Exception], action: object) -> None:
    try:
        action()  # type: ignore[operator]
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}")


def run_tests() -> None:
    now = datetime(2026, 1, 15, 9, tzinfo=timezone.utc)
    repository = FakeRepository()
    notifier = RecordingNotifier()
    service = IssueService(
        repository=repository,
        notifier=notifier,
        clock=FixedClock(now),
        id_factory=lambda: UUID(int=42),
    )
    issue = service.open_issue("API returns 500")
    assert repository.get(issue.id) is issue
    assert notifier.events == [(issue, now + timedelta(hours=24))]
    service.claim_issue(issue.id, "Lin")
    service.comment_on_issue(issue.id, "Deployed the fix")
    assert service.resolve_issue(issue.id).resolved is True
    expect_error(LookupError, lambda: service.resolve_issue(UUID(int=999)))
    print("Milestone 5 passed: service coordinates injected dependencies.")


if __name__ == "__main__":
    run_tests()
