#!/usr/bin/env bash
set -e
set -x

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python "${CURRENT_DIR}/app/tests_pre_start.py"

bash "${CURRENT_DIR}/scripts/test.sh" "$@"
