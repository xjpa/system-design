# 00 — Workstation, Linux, and Git

## Outcome

You can answer “what is running, as whom, with which configuration, and where is
its output?” before changing a system.

## Mental model

A process has an identity, parent, environment, working directory, open files,
and exit status. A service failure is often one of those facts disagreeing with
your expectation. Permissions are evaluated for an owner, group, and everyone
else; `sudo` is not a substitute for understanding which access is required.

## Lessons

1. Run `bash 10_process_inspection.sh`; inspect its PID with `ps`, then stop it
   gracefully with `kill` rather than closing the terminal.
2. Complete `20_triage.sh`. It must report command presence, disk capacity,
   memory, and the current user without changing the machine.
3. Create a temporary file with mode `600`, explain each digit, then compare
   with `644`. Do not practice recursive permission changes.
4. Create a branch, make one documentation edit, inspect `git diff`, and commit
   it with a message that states why. Do not push the practice commit unless
   you want it public.

Run `python3 check.py` after completing the TODOs.

## Operational artifact

Write `artifacts/00-command-journal.md` with five commands, what each measures,
and one unsafe variant to avoid. Record observations, not copied definitions.

## Reflection

- Why can a process be alive but not ready?
- What evidence would you collect before restarting an unknown service?
- Why is a small, reviewable Git commit useful during an incident?

## Definition of done

The check passes, you can find and stop the example process, and your journal
distinguishes observation commands from mutation commands.
