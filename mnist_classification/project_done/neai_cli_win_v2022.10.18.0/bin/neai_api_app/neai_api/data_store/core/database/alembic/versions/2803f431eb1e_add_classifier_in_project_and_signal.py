"""Add classifier in project and signal

Revision ID: 2803f431eb1e
Revises: 790fd2d121d3
Create Date: 2020-07-23 16:36:38.066399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2803f431eb1e'
down_revision = '790fd2d121d3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project', sa.Column('project_type', sa.String(100)))
    op.execute('UPDATE project SET project_type="on_board_training"')

    op.add_column('signal', sa.Column('class_name', sa.String(100)))




def downgrade():
    pass
