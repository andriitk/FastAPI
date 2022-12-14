"""Init

Revision ID: 7e5b6a69bada
Revises: 
Create Date: 2022-09-02 16:23:39.631715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e5b6a69bada'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ips',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('resource', sa.String(length=20), nullable=False),
    sa.Column('ip', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ips')
    # ### end Alembic commands ###
