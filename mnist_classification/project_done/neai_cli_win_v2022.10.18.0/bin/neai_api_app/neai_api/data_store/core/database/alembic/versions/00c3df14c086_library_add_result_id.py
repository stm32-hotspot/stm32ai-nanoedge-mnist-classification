"""Library: add result id

Revision ID: 00c3df14c086
Revises: d5d29061bb47
Create Date: 2020-01-08 15:13:28.487942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c3df14c086'
down_revision = 'd5d29061bb47'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('library',
                  sa.Column('result_id', sa.Integer)
                  )


def downgrade():
    op.drop_column('library', 'result_id')
