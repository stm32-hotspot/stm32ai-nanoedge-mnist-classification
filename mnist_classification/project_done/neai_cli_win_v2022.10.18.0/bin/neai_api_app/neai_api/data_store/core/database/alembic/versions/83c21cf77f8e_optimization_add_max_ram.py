"""Optimization: add max ram

Revision ID: 83c21cf77f8e
Revises: a4f38fdc1730
Create Date: 2019-09-11 14:16:30.652201

"""
from alembic import op
from sqlalchemy import Column, Integer


# revision identifiers, used by Alembic.
revision = '83c21cf77f8e'
down_revision = 'a4f38fdc1730'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  Column('max_ram', Integer, default=None)
                  )


def downgrade():
    op.drop_column('optimization', 'max_ram')
