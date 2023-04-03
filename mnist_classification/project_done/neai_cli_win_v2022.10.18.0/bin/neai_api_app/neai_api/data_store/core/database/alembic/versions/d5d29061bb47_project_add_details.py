"""Project add details

Revision ID: d5d29061bb47
Revises: 9ba3ec23ff66
Create Date: 2019-12-12 10:47:52.046389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d29061bb47'
down_revision = '9ba3ec23ff66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('details', sa.JSON))


def downgrade():
    pass
