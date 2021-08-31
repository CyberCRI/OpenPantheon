"""Refractor personality

Revision ID: 9f1fdf55725b
Revises: 6dd81729981f
Create Date: 2021-08-22 00:35:08.015342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f1fdf55725b'
down_revision = '6dd81729981f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personality', sa.Column('wikipedia_id', sa.String(), nullable=False))
    op.create_index(op.f('ix_personality_wikipedia_id'), 'personality', ['wikipedia_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_personality_wikipedia_id'), table_name='personality')
    op.drop_column('personality', 'wikipedia_id')
    # ### end Alembic commands ###