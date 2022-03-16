"""followers

Revision ID: 609a1c067b12
Revises: 3e3199c03503
Create Date: 2022-03-16 15:49:47.261830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '609a1c067b12'
down_revision = '3e3199c03503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###