"""Add OptimizationSignalAssociation table

Revision ID: e0c8ea83d191
Revises: 73486e03821f
Create Date: 2019-11-20 16:36:15.424888

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = 'e0c8ea83d191'
down_revision = '73486e03821f'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('x_optimization_signal',
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('optimization_id', sa.Integer, sa.ForeignKey('optimization.id')),
                    sa.Column('signal_id', sa.Integer, sa.ForeignKey('signal.id')),
                    sa.Column('relation_id', sa.Integer, default=0)
                    )

    op.execute('INSERT INTO x_optimization_signal (optimization_id, signal_id, relation_id) SELECT optimization_id, signal_id, 0 FROM optimization_signal')

    op.drop_table('optimization_signal')


def downgrade():
    pass
