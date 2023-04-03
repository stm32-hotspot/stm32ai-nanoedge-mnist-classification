"""Project: add settings

Revision ID: 17a7ff226eef
Revises: bb92a065f943
Create Date: 2021-01-14 11:10:57.552616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17a7ff226eef'
down_revision = 'bb92a065f943'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('settings', sa.JSON))


def downgrade():
    pass
