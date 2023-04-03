"""Library: remobe not null on mcu

Revision ID: 509b7af416f6
Revises: 00c3df14c086
Create Date: 2020-01-09 09:10:45.481365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '509b7af416f6'
down_revision = '00c3df14c086'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('library',
                  sa.Column('only_emulators', sa.Boolean)
                  )


def downgrade():
    op.drop_column('library', 'only_emulators')
