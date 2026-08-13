# Python Foundations and OOP Practice Lab

Start from Python syntax—including what `def` and `()` mean—then build the domain
layer of a small issue-tracking system. The lab eventually reaches the kind of
layered, testable OOP design you will see in a Python codebase at work.

Every lesson is one self-contained file containing a tutorial, worked example,
small TODOs, and checks. You never need to switch files while solving it.

## What you will learn

- classes, instances, class methods, properties, and Python's data model
- encapsulation and protecting business invariants
- composition versus inheritance
- abstract base classes and structural typing with `Protocol`
- polymorphism and the Strategy pattern
- dependency injection, repositories, services, and test doubles
- exceptions, type hints, dataclasses, assertions, and test doubles
- refactoring code without changing externally visible behavior

## Before you begin

The Foundations track assumes only that you can open a terminal and edit a text
file. It explicitly teaches variables, `def`, function calls, parameters,
`return`, conditions, loops, dictionaries, errors, classes, type hints,
properties, enums, dataclasses, and equality. Use Python 3.10 or newer.

No packages are needed for the main exercises:

```bash
cd oop-practice-lab
python foundations/00_how_to_use_these_lessons.py
```

Then open and run each numbered file in `foundations/`. A file may stop at its
first unfinished check. Implement one TODO, rerun the same command, and use the
new result as feedback. Each file runs independently.

## How to approach a programming problem

Do not try to hold the entire problem in your head. Use this loop:

1. Rewrite the requirement as one tiny input/output example.
2. Circle the syntax you recognize; look up only the first unfamiliar piece.
3. Run the starter before editing it and read the last error line.
4. Change one TODO—not the whole file—then rerun it.
5. When it passes, change an input and predict the result before rerunning.
6. Explain your solution aloud in ordinary language.

If stuck for 15 minutes, write down: “I expected ___, but got ___, on line ___.”
That is a strong debugging question to bring to a colleague or AI.

## Learning path

Complete these in order:

```text
foundations/00–01  running files, values, and variables
foundations/02–04  def, calls, parameters, and return
foundations/05–08  decisions, collections, and errors
foundations/09–10  classes, objects, and class practice
foundations/11–14  work-style syntax used by the OOP exercises
exercises/00–05    the issue-tracker OOP lab
```

Do not rush. One foundations file per study session is completely reasonable.
After file 10 you can try the BankAccount exercise; files 11–14 prepare you for
the denser syntax in the later OOP exercises.

## The scenario

Your team needs the core of an issue tracker. Users open issues, agents claim
them, people add comments, and issues move through a controlled lifecycle.
Different customer plans apply different response deadlines. An application
service coordinates persistence and notifications.

The target architecture is:

```text
caller -> IssueService -> Issue (domain behavior)
             |              |
             |              +-> ResponsePolicy (polymorphic strategy)
             +-> IssueRepository (port)
             +-> Notifier (port)
             +-> Clock (port)
```

Dependencies point inward: domain objects know nothing about databases, HTTP,
or email.

## Working loop

For every milestone:

1. Read the instructions, starter code, and `run_tests` function in that file.
2. Run the file and study the first failure.
3. Implement the smallest behavior that makes it pass.
4. Refactor names and structure while tests remain green.
5. Complete the short reflection prompt before moving on.

Exercise commands:

```bash
python exercises/00_bank_account.py
python exercises/01_value_objects.py
python exercises/02_issue_entity.py
python exercises/03_strategy.py
python exercises/04_repository.py
python exercises/05_service.py
```

## Milestone 0 — Your first useful class (1–2 hours)

File: `exercises/00_bank_account.py`

Implement `BankAccount`. You will learn what `class`, `self`, `__init__`,
methods, and properties mean while protecting a balance from invalid changes.
The file explains every feature beyond loops and basic functions that you need.

Reflection: Why should callers use `deposit` instead of changing the balance
directly?

## Milestone 1 — Value objects (2–3 hours)

File: `exercises/01_value_objects.py`

Implement `User`, `Comment`, and the enum-driven vocabulary. Requirements:

- Reject blank user names.
- Normalize email addresses by stripping whitespace and lowercasing.
- Compare users by their immutable ID, not by display name.
- Make `Comment` immutable after construction.
- Use timezone-aware timestamps.

Reflection: Why is a frozen comment safer than returning a mutable dictionary?
When should two objects be equal?

## Milestone 2 — A behavior-rich entity (4–5 hours)

File: `exercises/02_issue_entity.py`

Implement `Issue`. Keep lifecycle rules inside the entity rather than in the
caller:

- `Issue.open(...)` is the only public creation path.
- Titles cannot be blank and IDs are generated by the supplied factory.
- Expose comments as a read-only view; callers must use `add_comment`.
- Only agents can claim an issue.
- Allowed state transitions are `OPEN -> IN_PROGRESS -> RESOLVED` and
  `RESOLVED -> OPEN` (reopen). Invalid transitions raise a domain exception.
- Resolving requires an assignee and at least one comment.

Reflection: Which invalid states became impossible? What would break if callers
could assign directly to `issue.status` or append directly to its comments?

## Milestone 3 — Polymorphic policies (3–4 hours)

File: `exercises/03_strategy.py`

Implement three response-deadline strategies behind `ResponsePolicy`:

- `CommunityPolicy`: 72 hours for every priority.
- `BusinessPolicy`: 24 hours normally, 4 hours for high priority.
- `EnterprisePolicy`: 4 hours normally, 1 hour for high priority.

Add a new policy of your own without changing `Issue` or the existing policies.
This is the Open/Closed Principle in a small, useful form.

Reflection: Why is one strategy object preferable to conditionals scattered
through the service? Why is inheritance appropriate here but not for every code
reuse opportunity?

## Milestone 4 — Repository abstraction (3–4 hours)

File: `exercises/04_repository.py`

Implement `InMemoryIssueRepository` against the `IssueRepository` protocol.
It must save, update, fetch, list, and reject duplicate IDs. Do not leak its
internal dictionary from `list_all`.

Then write a `JsonIssueRepository` or SQLite adapter as a stretch exercise.
Neither the domain model nor the service should need to change.

Reflection: Is the in-memory repository a mock, fake, stub, or spy? What is
gained by depending on a protocol rather than a concrete database class?

## Milestone 5 — Application service and dependency injection (4–6 hours)

File: `exercises/05_service.py`

Implement the use cases in `IssueService`:

- open an issue, calculate its response deadline, persist it, and notify
- claim an issue and persist the change
- comment on an issue
- resolve an issue
- raise `LookupError` at the service boundary

The service receives its repository, notifier, clock, and ID factory in its
constructor. Its 24-hour response deadline is deliberately simple here; as a
stretch task, inject one of the policies from Milestone 3. Tests provide
deterministic fakes; production infrastructure could provide a real database,
email client, and system clock.

Reflection: Which dependencies are side effects? Why does injecting the clock
make the code easier to test?

## After the lab — Production hardening (optional)

Keep working in `exercises/05_service.py` and add one improvement at a time:

- Add pagination or filtering to repository queries.
- Add optimistic concurrency using an issue version number.
- Convert one requirement into a failing test before implementation.
- Add JSON serialization at the boundary without putting it in every entity.
- Add logging around use cases, but keep logging out of the domain model.
- Add a test at the bottom before implementing each improvement.

A real SWE repository eventually separates domain, service, infrastructure, and
tests into different files. This lab intentionally postpones that packaging
skill so it does not get in the way of learning OOP. Once these exercises feel
comfortable, splitting Milestone 5 into modules is a useful separate exercise.

## Definition of done

You are ready to move on when:

- all tests pass and you can explain every line you wrote;
- no public method allows an invalid lifecycle transition;
- domain code has no dependency on persistence or notification technology;
- a new policy and a new repository can be added without editing `Issue`;
- you can explain entity vs. value object, composition vs. inheritance,
  abstract base class vs. protocol, and fake vs. mock using this codebase;
- you can draw the dependency diagram above from memory;
- another person can clone the project and follow your README.

Score yourself after the final milestone (0 = cannot explain, 1 = can explain,
2 = can implement without guidance):

| Competency | 0–2 |
| --- | ---: |
| Model an entity and a value object | |
| Protect invariants through a small public API | |
| Choose composition or inheritance and justify it | |
| Define and implement an ABC and a protocol | |
| Inject side-effecting dependencies | |
| Write focused unit tests and useful fakes | |
| Refactor while preserving behavior | |
| Explain the architecture and its tradeoffs | |

A score of 13–16 means the OOP portion is in solid junior-SWE shape. A lower
score is a map of what to repeat, not a verdict. OOP is only one part of job
readiness; pair this lab with Git, SQL, HTTP/API work, debugging, data
structures, and collaborating through code review.

## Interview and code-review drills

After completing the lab, answer these aloud:

1. Why isn't OOP just “putting functions inside classes”?
2. Where does this design use encapsulation, abstraction, polymorphism, and
   inheritance?
3. Which SOLID principles are visible, and where could applying them further be
   needless complexity?
4. If two workers update one issue simultaneously, what can go wrong?
5. Where would transaction boundaries belong with a real database?
6. How would you expose these use cases through FastAPI without coupling the
   domain to FastAPI?
7. What would you change if comments could be edited or deleted?

## Hints policy

Use help in this order: type hints and docstrings, the failing assertion, Python
documentation, then a colleague or AI. When asking for help, request a hint or a
review of your reasoning before requesting a complete solution. The struggle to
translate a requirement into code is the exercise.
