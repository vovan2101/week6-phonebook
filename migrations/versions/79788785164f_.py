"""empty message

Revision ID: 79788785164f
Revises: 
Create Date: 2022-08-16 20:32:04.028150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79788785164f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###