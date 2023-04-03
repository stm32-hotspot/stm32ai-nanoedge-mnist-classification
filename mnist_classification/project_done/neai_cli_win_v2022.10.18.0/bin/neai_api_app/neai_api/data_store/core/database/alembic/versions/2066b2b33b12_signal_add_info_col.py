"""Signal: add info col

Revision ID: 2066b2b33b12
Revises: 63c13d8305a4
Create Date: 2022-08-10 11:01:28.394799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2066b2b33b12'
down_revision = '63c13d8305a4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('signal', sa.Column('info', sa.JSON))


def downgrade():
    pass
