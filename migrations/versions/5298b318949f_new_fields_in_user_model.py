"""new fields in user model

Revision ID: 5298b318949f
Revises: cc0b1fcffbcb
Create Date: 2022-03-05 10:41:04.357383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5298b318949f'
down_revision = 'cc0b1fcffbcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=280), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
