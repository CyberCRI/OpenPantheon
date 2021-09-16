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
from uvicorn.workers import UvicornWorker


class OpenPantheonUvicornWorker(UvicornWorker):
    """
    Add proxy headers to avoid issues with Uvicorn adding a `location` header
    pointing to the http endpoint
    """
    CONFIG_KWARGS = {"proxy_headers": True, "forwarded_allow_ips": "*"}
