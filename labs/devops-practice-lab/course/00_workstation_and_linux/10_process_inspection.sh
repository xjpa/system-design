#!/usr/bin/env bash
set -euo pipefail

# WORKED EXAMPLE: start a child, observe it, and clean it up on every exit path.
cleanup() {
  if [[ -n "${child_pid:-}" ]]; then
    kill "$child_pid" 2>/dev/null || true
    wait "$child_pid" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM

sleep 30 &
child_pid=$!
echo "Started child PID: $child_pid"
ps -o pid=,ppid=,user=,stat=,command= -p "$child_pid"
echo "Now try: ps -o pid,ppid,user,stat,command -p $child_pid"
echo "The trap will clean up the child when this script exits."
