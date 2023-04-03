"""Progression: add progression type column

Revision ID: f014334ea2b1
Revises: 918613715f21
Create Date: 2021-05-04 10:21:36.512303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f014334ea2b1'
down_revision = '918613715f21'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('progression',
                  sa.Column('progression_type', sa.String)
                  )


def downgrade():
    op.drop_column('progression', 'progression_type')
