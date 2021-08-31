"""Add a few columns to person

Revision ID: 6dd81729981f
Revises: 40adcb56bd8d
Create Date: 2021-08-18 00:28:16.437288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6dd81729981f'
down_revision = '40adcb56bd8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personality', sa.Column('name', sa.String(), nullable=True))
    op.add_column('personality', sa.Column('image', sa.String(), nullable=True))
    op.add_column('personality', sa.Column('job', sa.String(), nullable=True))
    op.add_column('personality', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('personality', sa.Column('comments', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.drop_index('ix_personality_title', table_name='personality')
    op.create_index(op.f('ix_personality_gender'), 'personality', ['gender'], unique=False)
    op.create_index(op.f('ix_personality_image'), 'personality', ['image'], unique=False)
    op.create_index(op.f('ix_personality_job'), 'personality', ['job'], unique=False)
    op.create_index(op.f('ix_personality_name'), 'personality', ['name'], unique=False)
    op.drop_column('personality', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personality', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_personality_name'), table_name='personality')
    op.drop_index(op.f('ix_personality_job'), table_name='personality')
    op.drop_index(op.f('ix_personality_image'), table_name='personality')
    op.drop_index(op.f('ix_personality_gender'), table_name='personality')
    op.create_index('ix_personality_title', 'personality', ['title'], unique=False)
    op.drop_column('personality', 'comments')
    op.drop_column('personality', 'gender')
    op.drop_column('personality', 'job')
    op.drop_column('personality', 'image')
    op.drop_column('personality', 'name')
    # ### end Alembic commands ###