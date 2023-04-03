"""Signal: update with repair

Revision ID: 93f9e307f5fe
Revises: 19218c055328
Create Date: 2019-09-13 10:43:03.159447

"""
from alembic import op
from sqlalchemy import Column, Integer, JSON


# revision identifiers, used by Alembic.
revision = '93f9e307f5fe'
down_revision = '19218c055328'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('signal') as batch_op:
        batch_op.drop_column('repaired_file_name')
        batch_op.add_column(Column('repaired_from_signal_id', Integer, default=None))
        batch_op.add_column(Column('repairs_report', JSON, default=None))


def downgrade():
    pass
