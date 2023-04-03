"""Project: add content field

Revision ID: c0f37a0cf93b
Revises: 93f9e307f5fe
Create Date: 2019-09-27 09:51:38.445916

"""
from alembic import op
from sqlalchemy import Column, BLOB


# revision identifiers, used by Alembic.
revision = 'c0f37a0cf93b'
down_revision = '93f9e307f5fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('project',
                  Column('content_encoded', BLOB)
                  )


def downgrade():
    op.drop_column('project', 'content_encoded')
