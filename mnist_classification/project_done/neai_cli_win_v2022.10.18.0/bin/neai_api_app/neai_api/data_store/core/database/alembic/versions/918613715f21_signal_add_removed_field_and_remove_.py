"""Signal: add removed field and remove repairs fields

Revision ID: 918613715f21
Revises: 17a7ff226eef
Create Date: 2021-03-17 11:51:27.777915

"""
from alembic import op
from sqlalchemy import Column, Boolean


# revision identifiers, used by Alembic.
revision = '918613715f21'
down_revision = '17a7ff226eef'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('signal') as batch_op:
        batch_op.drop_column('repaired_from_signal_id')
        batch_op.drop_column('repairs_report')
        batch_op.add_column(Column('removed', Boolean))


def downgrade():
    pass
