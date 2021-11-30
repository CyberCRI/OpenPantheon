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

# Exit in case of error
set -e

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "${CURRENT_DIR}/.."

EMAIL_TEMPLATES_MJML=`find ./backend/app/app/email-templates/src/ -type f -name '*.mjml'`

for EMAIL_TEMPLATE_MJML in ${EMAIL_TEMPLATES_MJML}; do
  EMAIL_TEMPLATE_HTML=`echo "$EMAIL_TEMPLATE_MJML" | sed -E 's/^(.*\/)src(\/.*)\.mjml$/\1\build\2.html/'`
  ./frontend/node_modules/.bin/mjml -l strict --config.minify true --config.beautify false "$EMAIL_TEMPLATE_MJML" -o "$EMAIL_TEMPLATE_HTML"
done
