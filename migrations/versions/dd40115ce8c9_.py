"""empty message

Revision ID: dd40115ce8c9
Revises: 
Create Date: 2022-09-25 14:52:46.083328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd40115ce8c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products_categories', sa.Column('product_category_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products_categories', 'product_category_description')
    # ### end Alembic commands ###
