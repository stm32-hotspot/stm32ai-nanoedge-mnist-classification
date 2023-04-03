"""Add is_multivariate in project

Revision ID: 0da43b423de2
Revises: 509b7af416f6
Create Date: 2020-04-08 12:06:02.752628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0da43b423de2'
down_revision = '509b7af416f6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('is_multivariate', sa.Boolean, nullable=True))
    op.execute('UPDATE project SET is_multivariate=0')


def downgrade():
    pass
