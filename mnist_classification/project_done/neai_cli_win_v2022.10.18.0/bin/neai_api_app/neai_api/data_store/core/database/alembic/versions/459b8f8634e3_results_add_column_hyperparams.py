"""Results: add column hyperparams

Revision ID: 459b8f8634e3
Revises: f014334ea2b1
Create Date: 2021-08-10 11:21:09.665476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '459b8f8634e3'
down_revision = 'f014334ea2b1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result', sa.Column('hyperparams', sa.BLOB, nullable=True))


def downgrade():
    pass
