"""Debugging time_created

Revision ID: 42bad993972d
Revises: bdc3c703d0cc
Create Date: 2021-09-09 18:49:42.595204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42bad993972d'
down_revision = 'bdc3c703d0cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'fluff',
               existing_type=sa.VARCHAR(),
               type_=sa.PickleType(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'fluff',
               existing_type=sa.PickleType(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    # ### end Alembic commands ###