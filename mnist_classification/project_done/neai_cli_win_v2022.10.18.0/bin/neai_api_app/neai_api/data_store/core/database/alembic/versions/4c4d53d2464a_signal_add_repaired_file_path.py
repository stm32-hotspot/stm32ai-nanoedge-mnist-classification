"""Signal: add repaired_file_path

Revision ID: 4c4d53d2464a
Revises: 7223ec8c3396
Create Date: 2019-09-04 15:55:46.752177

"""
from alembic import op
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = '4c4d53d2464a'
down_revision = '7223ec8c3396'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('signal',
                  Column('repaired_file_name', String(255))
                  )


def downgrade():
    op.drop_column('signal', 'repaired_file_name')
