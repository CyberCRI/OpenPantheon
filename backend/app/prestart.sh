#!/usr/bin/env bash
# OpenPantheon: the pantheon for Education
# Copyright (C) 2021 CRI
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

set -e
set -x

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Let the DB start
python "${CURRENT_DIR}/app/backend_pre_start.py"

# Run migrations
alembic upgrade head

# Create initial data in DB
python "${CURRENT_DIR}/app/initial_data.py"
