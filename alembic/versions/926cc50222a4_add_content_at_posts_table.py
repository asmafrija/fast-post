"""add content at posts table

Revision ID: 926cc50222a4
Revises: 01bb8161d3cb
Create Date: 2022-04-11 04:22:07.625607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '926cc50222a4'
down_revision = '01bb8161d3cb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
