"""create users table

Revision ID: 01bb8161d3cb
Revises: bbf931fe2bcc
Create Date: 2022-04-11 04:02:49.296792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01bb8161d3cb'
down_revision = 'bbf931fe2bcc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
