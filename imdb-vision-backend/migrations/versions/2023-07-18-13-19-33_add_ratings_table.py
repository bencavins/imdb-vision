"""add ratings table

Revision ID: e18b26a038fb
Revises: 805101fa6f39
Create Date: 2023-07-18 13:19:33.681493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e18b26a038fb'
down_revision = '805101fa6f39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imdb_id', sa.String(), nullable=False),
    sa.Column('average_rating', sa.Float(), nullable=True),
    sa.Column('num_votes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['imdb_id'], ['episodes.imdb_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    # ### end Alembic commands ###