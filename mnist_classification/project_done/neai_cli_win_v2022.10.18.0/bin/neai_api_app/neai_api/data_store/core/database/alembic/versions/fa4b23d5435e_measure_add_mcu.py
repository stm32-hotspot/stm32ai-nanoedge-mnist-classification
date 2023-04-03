"""Measure: add mcu

Revision ID: fa4b23d5435e
Revises: c0f37a0cf93b
Create Date: 2019-09-30 10:06:58.080797

"""
from alembic import op
from sqlalchemy import Column, String

# revision identifiers, used by Alembic.
revision = 'fa4b23d5435e'
down_revision = 'c0f37a0cf93b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('measure',
                  Column('mcu', String(255))
                  )


def downgrade():
    op.drop_column('measure', 'mcu')
