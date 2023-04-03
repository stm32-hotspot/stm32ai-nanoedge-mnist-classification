"""Result: Add commit_tag_used

Revision ID: 1ad31a3fbb67
Revises: 44df7c460d68
Create Date: 2019-08-30 14:43:36.021736

"""
from alembic import op
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = '1ad31a3fbb67'
down_revision = '44df7c460d68'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result',
                  Column('commit_tag_used', String(20))
                  )


def downgrade():
    op.drop_column('result', 'commit_tag_used')

