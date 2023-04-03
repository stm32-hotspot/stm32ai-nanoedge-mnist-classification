"""Optimizer: add info column

Revision ID: 73486e03821f
Revises: 24a0666561c9
Create Date: 2019-11-14 15:52:59.353353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73486e03821f'
down_revision = '24a0666561c9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  sa.Column('info', sa.JSON)
                  )


def downgrade():
    op.drop_column('optimization', 'info')
