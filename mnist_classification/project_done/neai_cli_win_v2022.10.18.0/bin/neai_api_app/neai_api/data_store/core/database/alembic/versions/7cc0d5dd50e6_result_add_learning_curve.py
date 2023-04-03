"""Result: add learning curve

Revision ID: 7cc0d5dd50e6
Revises: e0c8ea83d191
Create Date: 2019-11-22 10:06:07.308577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cc0d5dd50e6'
down_revision = 'e0c8ea83d191'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result',
                  sa.Column('learning_curve', sa.JSON)
                  )


def downgrade():
    op.drop_column('result', 'learning_curve')
