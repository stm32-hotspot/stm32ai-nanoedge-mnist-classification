"""Progression: add progression date

Revision ID: e11775dffbd4
Revises: 83c21cf77f8e
Create Date: 2019-09-11 16:41:33.621811

"""
from alembic import op
from datetime import datetime
from sqlalchemy import Column, DateTime


# revision identifiers, used by Alembic.
revision = 'e11775dffbd4'
down_revision = '83c21cf77f8e'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('progession', 'progression')
    op.add_column('progression',
                  Column('update_date', DateTime, default=datetime.utcnow())
                  )


def downgrade():
    op.drop_column('progression', 'update_date')
