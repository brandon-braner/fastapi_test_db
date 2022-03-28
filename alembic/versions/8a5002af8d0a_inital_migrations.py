"""inital migrations

Revision ID: 8a5002af8d0a
Revises: 
Create Date: 2022-03-27 22:15:37.607435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a5002af8d0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('tax', sa.Float, nullable=False),
        sa.Column('total', sa.Float, nullable=False),
        sa.Column('status', sa.String),
    )


def downgrade():
    op.drop_table('transactions')
