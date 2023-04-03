"""Optimizer: add best_result_id

Revision ID: 61545f00e8a6
Revises: 933447233b14
Create Date: 2020-12-08 11:38:34.477025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61545f00e8a6'
down_revision = '933447233b14'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  sa.Column('best_result_id', sa.Integer)
                  )


def downgrade():
    op.drop_column('optimization', 'best_result_id')
