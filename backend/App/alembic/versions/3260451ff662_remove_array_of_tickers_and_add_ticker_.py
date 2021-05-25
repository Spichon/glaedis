"""remove array of tickers and add ticker in portfolio

Revision ID: 3260451ff662
Revises: f95b9eb86cc3
Create Date: 2021-05-23 11:03:19.108554

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3260451ff662'
down_revision = 'f95b9eb86cc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('broker', 'tickers')
    op.alter_column('portfolio', 'ticker',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('portfolio', 'ticker',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.add_column('broker', sa.Column('tickers', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###