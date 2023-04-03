"""Result: change model and combination to BLOB & Library: remove combination

Revision ID: 325326986afe
Revises: c019bb2b3b3f
Create Date: 2019-11-07 15:04:29.920736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325326986afe'
down_revision = 'c019bb2b3b3f'
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table('result') as batch_op:
        batch_op.drop_column('combination')
        batch_op.add_column(sa.Column('combination', sa.BLOB))
        batch_op.drop_column('model')
        batch_op.add_column(sa.Column('model', sa.BLOB))

    with op.batch_alter_table('library') as batch_op:
        batch_op.drop_column('combination')


def downgrade():
    pass
