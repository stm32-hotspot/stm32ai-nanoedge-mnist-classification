"""Results: add precision, confidence and details

Revision ID: 81299ed8d725
Revises: 2803f431eb1e
Create Date: 2020-07-30 09:17:11.114352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81299ed8d725'
down_revision = '2803f431eb1e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result', sa.Column('precision', sa.Float()))
    op.add_column('result', sa.Column('confidence', sa.Float()))
    op.add_column('result', sa.Column('details', sa.JSON()))

    op.execute('UPDATE result SET precision=balanced_accuracy, confidence=transformed_functional_margin')


def downgrade():
    pass
