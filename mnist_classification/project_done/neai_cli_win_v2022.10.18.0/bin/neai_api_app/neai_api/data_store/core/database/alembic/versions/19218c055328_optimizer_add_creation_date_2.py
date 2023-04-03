"""Optimizer: add creation date 2

Revision ID: 19218c055328
Revises: e11775dffbd4
Create Date: 2019-09-12 13:54:53.459438

"""
from alembic import op
from _datetime import datetime
from sqlalchemy import Column, DateTime


# revision identifiers, used by Alembic.
revision = '19218c055328'
down_revision = 'e11775dffbd4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  Column('creation_date', DateTime, default=datetime.utcnow())
                  )


def downgrade():
    op.drop_column('optimization', 'creation_date')
