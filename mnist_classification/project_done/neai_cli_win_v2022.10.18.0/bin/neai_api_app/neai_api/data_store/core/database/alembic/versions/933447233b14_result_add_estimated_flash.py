"""Result: add estimated flash

Revision ID: 933447233b14
Revises: 81299ed8d725
Create Date: 2020-09-29 10:32:43.573443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '933447233b14'
down_revision = '81299ed8d725'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result', sa.Column('estimated_flash', sa.Float()))


def downgrade():
    pass
