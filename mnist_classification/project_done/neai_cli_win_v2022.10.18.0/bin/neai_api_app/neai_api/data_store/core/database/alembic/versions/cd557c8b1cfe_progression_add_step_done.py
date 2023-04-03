"""Progression: add step done

Revision ID: cd557c8b1cfe
Revises: 7cc0d5dd50e6
Create Date: 2019-11-22 14:01:59.149961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd557c8b1cfe'
down_revision = '7cc0d5dd50e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('progression',
                  sa.Column('step_done', sa.String)
                  )


def downgrade():
    op.drop_column('progression', 'step_done')
