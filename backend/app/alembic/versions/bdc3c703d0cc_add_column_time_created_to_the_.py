"""Add column time_created to the personality

Revision ID: bdc3c703d0cc
Revises: 030be1df4bec
Create Date: 2021-09-07 09:01:45.122271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdc3c703d0cc'
down_revision = '030be1df4bec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personality', sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('personality', sa.Column('field', sa.String(), nullable=True))
    op.drop_index('ix_personality_description', table_name='personality')
    op.drop_index('ix_personality_image', table_name='personality')
    op.drop_index('ix_personality_job', table_name='personality')
    op.drop_index('ix_personality_name', table_name='personality')
    op.create_index(op.f('ix_personality_field'), 'personality', ['field'], unique=False)
    op.drop_constraint('personality_owner_id_fkey', 'personality', type_='foreignkey')
    op.drop_column('personality', 'job')
    op.drop_column('personality', 'owner_id')
    op.drop_column('personality', 'image')
    op.drop_column('personality', 'description')
    op.drop_column('personality', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personality', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('personality', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('personality', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('personality', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('personality', sa.Column('job', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('personality_owner_id_fkey', 'personality', 'user', ['owner_id'], ['id'])
    op.drop_index(op.f('ix_personality_field'), table_name='personality')
    op.create_index('ix_personality_name', 'personality', ['name'], unique=False)
    op.create_index('ix_personality_job', 'personality', ['job'], unique=False)
    op.create_index('ix_personality_image', 'personality', ['image'], unique=False)
    op.create_index('ix_personality_description', 'personality', ['description'], unique=False)
    op.drop_column('personality', 'field')
    op.drop_column('personality', 'time_created')
    # ### end Alembic commands ###