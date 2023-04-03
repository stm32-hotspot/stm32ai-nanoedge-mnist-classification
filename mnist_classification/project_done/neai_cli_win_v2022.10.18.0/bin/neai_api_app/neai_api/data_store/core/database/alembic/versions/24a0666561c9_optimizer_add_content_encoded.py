"""Optimizer: add content_encoded

Revision ID: 24a0666561c9
Revises: 325326986afe
Create Date: 2019-11-14 13:59:00.026268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24a0666561c9'
down_revision = '325326986afe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('optimization',
                  sa.Column('content_encoded', sa.BLOB)
                  )


def downgrade():
    op.drop_column('optimization', 'content_encoded')
