"""create posts table

Revision ID: 124a19cf8e2b
Revises: 
Create Date: 2022-08-18 14:12:32.995627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '124a19cf8e2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    pass
