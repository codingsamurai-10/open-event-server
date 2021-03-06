"""empty message

Revision ID: 507022789bcb
Revises: 286869159bb5
Create Date: 2020-07-26 08:15:09.725288

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '507022789bcb'
down_revision = '286869159bb5'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('instagram_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'instagram_url')
    # ### end Alembic commands ###
