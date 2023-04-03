"""Project: add is_compatible

Revision ID: 9ba3ec23ff66
Revises: cd963f063239
Create Date: 2019-11-27 09:40:42.471190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba3ec23ff66'
down_revision = 'cd963f063239'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('is_compatible', sa.Boolean, default=True))


def downgrade():
    pass
