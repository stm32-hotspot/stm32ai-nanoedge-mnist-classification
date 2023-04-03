"""Result: add x_val_idx

Revision ID: 790fd2d121d3
Revises: 104b73b47179
Create Date: 2020-06-08 10:51:17.507188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790fd2d121d3'
down_revision = '104b73b47179'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result', sa.Column('x_val_idx', sa.Integer, nullable=True))


def downgrade():
    pass
