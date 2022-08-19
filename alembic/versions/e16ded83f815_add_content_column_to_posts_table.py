"""add content Column to posts table

Revision ID: e16ded83f815
Revises: 124a19cf8e2b
Create Date: 2022-08-18 14:50:32.783053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e16ded83f815'
down_revision = '124a19cf8e2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
