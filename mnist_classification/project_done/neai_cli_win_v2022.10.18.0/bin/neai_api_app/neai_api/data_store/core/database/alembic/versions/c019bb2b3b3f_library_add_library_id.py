"""Library: add library id

Revision ID: c019bb2b3b3f
Revises: cea7c2c3ff7b
Create Date: 2019-11-07 10:59:17.995327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c019bb2b3b3f'
down_revision = 'cea7c2c3ff7b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('library',
                  sa.Column('library_id', sa.String(100))
                  )


def downgrade():
    op.drop_column('library', 'library_id')
