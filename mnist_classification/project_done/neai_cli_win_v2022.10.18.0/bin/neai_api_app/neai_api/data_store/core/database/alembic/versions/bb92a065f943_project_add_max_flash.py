"""Project: add max_flash

Revision ID: bb92a065f943
Revises: 61545f00e8a6
Create Date: 2020-12-11 12:47:55.486359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb92a065f943'
down_revision = '61545f00e8a6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('max_flash', sa.Integer, nullable=True))


def downgrade():
    pass
