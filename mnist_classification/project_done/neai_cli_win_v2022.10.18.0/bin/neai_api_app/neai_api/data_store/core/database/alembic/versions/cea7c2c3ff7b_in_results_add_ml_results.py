"""In results, add ml_results

Revision ID: cea7c2c3ff7b
Revises: 4254be88d8d6
Create Date: 2019-10-18 11:27:02.731866

"""
from alembic import op
from sqlalchemy import Column, JSON


# revision identifiers, used by Alembic.
revision = 'cea7c2c3ff7b'
down_revision = '4254be88d8d6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('result',
                  Column('ml_results', JSON)
                  )


def downgrade():
    op.drop_column('result', 'ml_results')
