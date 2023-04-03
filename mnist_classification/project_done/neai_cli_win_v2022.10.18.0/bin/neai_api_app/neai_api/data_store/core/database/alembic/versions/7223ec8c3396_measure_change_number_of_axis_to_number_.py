"""Measure: change number_of_axis to number_axis

Revision ID: 7223ec8c3396
Revises: 1ad31a3fbb67
Create Date: 2019-09-03 14:03:44.535199

"""
from alembic import op
from sqlalchemy import Column, Integer


# revision identifiers, used by Alembic.
revision = '7223ec8c3396'
down_revision = '1ad31a3fbb67'
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table('measure') as batch_op:
        batch_op.add_column(Column('number_axis', Integer, default=1))
        batch_op.drop_column('number_of_axis')


def downgrade():
    pass
