"""empty message

Revision ID: 09ed7318a803
Revises: 4b20e46a6ea5
Create Date: 2019-07-04 16:15:58.535319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09ed7318a803'
down_revision = '4b20e46a6ea5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('uid', sa.String(length=255), nullable=True))
    op.drop_column('products', '_uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('_uid', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('products', 'uid')
    # ### end Alembic commands ###