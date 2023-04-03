"""Results: add kpis col

Revision ID: ff6d6031eb4b
Revises: 459b8f8634e3
Create Date: 2022-05-10 10:49:45.030597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff6d6031eb4b'
down_revision = '459b8f8634e3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result', sa.Column('kpis', sa.JSON))


def downgrade():
    pass
