"""In library, add specifications

Revision ID: 4254be88d8d6
Revises: fa4b23d5435e
Create Date: 2019-10-18 09:21:22.712395

"""
from alembic import op
from sqlalchemy import Column, JSON


# revision identifiers, used by Alembic.
revision = '4254be88d8d6'
down_revision = 'fa4b23d5435e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('library',
                  Column('specifications', JSON)
                  )


def downgrade():
    op.drop_column('library', 'specifications')
