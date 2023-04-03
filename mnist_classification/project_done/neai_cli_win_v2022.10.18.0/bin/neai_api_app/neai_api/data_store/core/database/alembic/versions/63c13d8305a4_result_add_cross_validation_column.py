"""Result: add cross validation column

Revision ID: 63c13d8305a4
Revises: ff6d6031eb4b
Create Date: 2022-05-16 11:28:27.498626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c13d8305a4'
down_revision = 'ff6d6031eb4b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result', sa.Column('cross_validation', sa.JSON))


def downgrade():
    pass
