"""Optimizer: Add commit_tag_used

Revision ID: 44df7c460d68
Revises: 354dc06dc412
Create Date: 2019-08-30 13:33:19.893548

"""
from alembic import op
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = '44df7c460d68'
down_revision = '354dc06dc412'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  Column('commit_tag_used', String(20))
                  )


def downgrade():
    op.drop_column('optimization', 'commit_tag_used')
