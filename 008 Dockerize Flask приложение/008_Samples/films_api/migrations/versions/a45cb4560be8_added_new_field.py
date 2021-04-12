"""added new field

Revision ID: a45cb4560be8
Revises: a5f6ea9ad79a
Create Date: 2020-11-26 20:30:59.982450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45cb4560be8'
down_revision = 'a5f6ea9ad79a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('test', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'test')
    # ### end Alembic commands ###
