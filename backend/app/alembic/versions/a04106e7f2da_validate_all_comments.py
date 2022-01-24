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
"""validate_all_comments

Revision ID: a04106e7f2da
Revises: cbe8d48305cb
Create Date: 2022-01-24 13:56:47.078269

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'a04106e7f2da'
down_revision = 'cbe8d48305cb'
branch_labels = None
depends_on = 'cbe8d48305cb'

comment = sa.table('comment', sa.Column('is_validated', sa.Boolean()))


def upgrade():
    op.execute(comment.update().where(comment.c.is_validated == op.inline_literal(False)).values(
        {'is_validated': op.inline_literal(True)}))


def downgrade():
    pass
