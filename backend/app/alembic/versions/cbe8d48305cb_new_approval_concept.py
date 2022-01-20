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
"""new approval concept

Revision ID: cbe8d48305cb
Revises: 1c887bb157b0
Create Date: 2022-01-19 11:31:01.076796

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'cbe8d48305cb'
down_revision = '1c887bb157b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('is_validated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'is_validated')
    # ### end Alembic commands ###