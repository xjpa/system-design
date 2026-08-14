"""LESSON 08.20: Application-service workflow drills.

Run: python course/08_oop_architecture/20_service_workflow_drills.py

An application service usually follows a short orchestration recipe:

    validate boundary input -> load/create domain object -> invoke behavior
    -> persist -> trigger external side effect -> return a useful result

The service coordinates. The domain object still owns its business rules.
"""

from dataclasses import dataclass, field
from typing import Protocol


# WORKED EXAMPLE — receive a dependency and coordinate one action
class Prefixer:
    def add_prefix(self, text: str) -> str:
        return "TASK: " + text


class LabelService:
    def __init__(self, prefixer: Prefixer) -> None:
        self.prefixer = prefixer

    def make_label(self, text: str) -> str:
        return self.prefixer.add_prefix(text)


assert LabelService(Prefixer()).make_label("Practice") == "TASK: Practice"


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    def complete(self) -> None:
        if self.completed:
            raise ValueError("task is already complete")
        self.completed = True


class TaskRepository(Protocol):
    def add(self, task: Task) -> None: ...

    def get(self, task_id: int) -> Task | None: ...

    def update(self, task: Task) -> None: ...


class EventSink(Protocol):
    def publish(self, event_name: str, task: Task) -> None: ...


class TaskService:
    def __init__(
        self,
        repository: TaskRepository,
        events: EventSink,
        id_factory,
    ) -> None:
        # TODO: store all three injected dependencies.
        raise NotImplementedError

    def create_task(self, title: str) -> Task:
        # TODO: strip and validate title at this input boundary.
        # TODO: create with the injected ID, add, publish "task.created", return.
        raise NotImplementedError

    def complete_task(self, task_id: int) -> Task:
        # TODO: load through _require_task, invoke complete, update,
        # publish "task.completed", and return the task.
        raise NotImplementedError

    def _require_task(self, task_id: int) -> Task:
        # TODO: get the task and translate a missing result into LookupError.
        raise NotImplementedError


class FakeTaskRepository:
    def __init__(self) -> None:
        self.items: dict[int, Task] = {}
        self.calls: list[tuple[str, int]] = []

    def add(self, task: Task) -> None:
        # TODO: store the task and record ("add", task.id).
        raise NotImplementedError

    def get(self, task_id: int) -> Task | None:
        # TODO: record ("get", task_id) and return the task or None.
        raise NotImplementedError

    def update(self, task: Task) -> None:
        # TODO: store the task and record ("update", task.id).
        raise NotImplementedError


@dataclass
class RecordingEventSink:
    events: list[tuple[str, Task]] = field(default_factory=list)

    def publish(self, event_name: str, task: Task) -> None:
        # TODO: append the event tuple.
        raise NotImplementedError


def expect_error(error_type, action) -> None:
    try:
        action()
    except error_type:
        return
    raise AssertionError("Expected " + error_type.__name__)


repository = FakeTaskRepository()
events = RecordingEventSink()
service = TaskService(repository, events, id_factory=lambda: 101)

task = service.create_task("  Practice dependency injection  ")
assert task == Task(101, "Practice dependency injection")
assert repository.items[101] is task
assert events.events == [("task.created", task)]

completed = service.complete_task(101)
assert completed.completed is True
assert repository.calls == [("add", 101), ("get", 101), ("update", 101)]
assert events.events[-1] == ("task.completed", task)
expect_error(LookupError, lambda: service.complete_task(999))
expect_error(ValueError, lambda: service.create_task(" "))

# TRANSFER CHALLENGE:
# Add rename_task(task_id, new_title). Decide which title rule belongs on Task,
# then test the repository call and a "task.renamed" event.

print("Lesson 08.20 passed: the service orchestrates injected collaborators.")
