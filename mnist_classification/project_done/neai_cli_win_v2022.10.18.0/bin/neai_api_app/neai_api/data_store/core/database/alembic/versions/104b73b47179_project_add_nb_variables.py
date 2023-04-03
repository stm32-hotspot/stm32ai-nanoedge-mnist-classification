"""Project: add nb_variables

Revision ID: 104b73b47179
Revises: 0da43b423de2
Create Date: 2020-05-26 15:11:32.303804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104b73b47179'
down_revision = '0da43b423de2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('nb_variables', sa.Integer, nullable=True))


def downgrade():
    pass
