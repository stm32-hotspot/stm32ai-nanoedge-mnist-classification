"""Remove Measure table

Revision ID: cd963f063239
Revises: cd557c8b1cfe
Create Date: 2019-11-26 13:20:04.432606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd963f063239'
down_revision = 'cd557c8b1cfe'
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table('project') as batch_op:
        batch_op.add_column(sa.Column('mcu', sa.String(255)))
        batch_op.add_column(sa.Column('number_axis', sa.Integer, default=1))
        batch_op.add_column(sa.Column('max_ram', sa.Integer, default=200000))

    op.execute('''UPDATE project
                  SET
                        mcu=(SELECT mcu from measure where id=1),
                        number_axis=(SELECT number_axis from measure where id=1),
                        max_ram=(SELECT max_ram from measure where id=1)
        ''')

    op.drop_table('measure')


def downgrade():
    pass
