"""empty message

Revision ID: 53798378e848
Revises: 174656f6b8e4
Create Date: 2019-12-09 17:57:46.505322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53798378e848'
down_revision = '174656f6b8e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['commenter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'commenter_id')
    op.drop_table('users')
    # ### end Alembic commands ###
