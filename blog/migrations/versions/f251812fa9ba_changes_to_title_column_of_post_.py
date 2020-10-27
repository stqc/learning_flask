"""changes to Title column of post_uploaded title has to be unique

Revision ID: f251812fa9ba
Revises: 2c7457303f5e
Create Date: 2020-10-27 20:41:56.542521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f251812fa9ba'
down_revision = '2c7457303f5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'post_uploaded', ['Title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post_uploaded', type_='unique')
    # ### end Alembic commands ###
