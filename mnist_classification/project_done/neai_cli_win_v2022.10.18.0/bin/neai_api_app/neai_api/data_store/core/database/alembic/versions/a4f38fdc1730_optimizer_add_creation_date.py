"""Optimizer: add creation date

Revision ID: a4f38fdc1730
Revises: 4c4d53d2464a
Create Date: 2019-09-10 11:32:28.797666

"""
from alembic import op
from sqlalchemy import Column, Integer


# revision identifiers, used by Alembic.
revision = 'a4f38fdc1730'
down_revision = '4c4d53d2464a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  Column('nb_cols_to_use', Integer)
                  )


def downgrade():
    op.drop_column('optimization', 'nb_cols_to_use')
