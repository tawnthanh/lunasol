"""create users table

Revision ID: 6327ed0403e8
Revises: 
Create Date: 2020-09-30 14:11:26.738620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34b32b995a12'
down_revision = '6327ed0403e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('birth_month', sa.String(length=100), nullable=False),
    sa.Column('birth_day', sa.Integer(), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=False),
    sa.Column('birth_hour', sa.Integer(), nullable=False),
    sa.Column('birth_minutes', sa.Integer(), nullable=False),
    sa.Column('birth_am_pm', sa.String(length=2), nullable=False),
    sa.Column('state_id', sa.Integer(), sa.ForeignKey('states.id'), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
    sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
