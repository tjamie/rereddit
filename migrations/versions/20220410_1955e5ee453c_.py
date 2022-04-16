"""empty message

Revision ID: 1955e5ee453c
Revises: 15f125fa3a70
Create Date: 2022-04-10 15:58:00.072477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1955e5ee453c'
down_revision = '15f125fa3a70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###
