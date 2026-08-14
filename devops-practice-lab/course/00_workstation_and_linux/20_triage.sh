#!/usr/bin/env bash
set -euo pipefail

require_command() {
  local command_name="$1"
  # TODO: return success when command_name is available on PATH, failure otherwise.
  return 1
}

disk_summary() {
  # TODO: show human-readable capacity for the current filesystem without modifying it.
  echo "TODO"
}

echo "user=$(id -un)"
echo "shell=${SHELL:-unknown}"
require_command python3
disk_summary
