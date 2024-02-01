"""added foreign key

Revision ID: 0c8078613752
Revises: d7a0bd7cfff2
Create Date: 2024-02-01 08:43:15.616837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8078613752'
down_revision = 'd7a0bd7cfff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('foreign_key_constraint', 'users', ['poster_id'], ['id'])
        batch_op.drop_column('author')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###