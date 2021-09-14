#!/usr/bin/env bash

set -e
set -x

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Let the DB start
python "${CURRENT_DIR}/app/backend_pre_start.py"

# Run migrations
alembic upgrade head

# Create initial data in DB
python "${CURRENT_DIR}/app/initial_data.py"
