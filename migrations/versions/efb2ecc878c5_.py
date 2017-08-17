"""empty message

Revision ID: efb2ecc878c5
Revises: 04060417378c
Create Date: 2016-07-04 13:21:26.744000

"""

# revision identifiers, used by Alembic.
revision = 'efb2ecc878c5'
down_revision = '04060417378c'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'color')
    op.drop_column('events_version', 'color')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events_version', sa.Column('color', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('events', sa.Column('color', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    ### end Alembic commands ###