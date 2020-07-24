"""Initial migration - Created user table

Revision ID: 10225403a36e
Revises: 
Create Date: 2020-07-24 06:34:32.510237

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '10225403a36e'
down_revision = None
branch_labels = None
depends_on = None

gender_enum = postgresql.ENUM('male', 'female', 'other', name='enum_gender')
role_enum = postgresql.ENUM('candidate', 'employer', name='enum_role')


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    gender_enum.create(op.get_bind())
    role_enum.create(op.get_bind())

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # Enum columns
    op.add_column('user', sa.Column('gender', gender_enum, nullable=True))
    op.add_column('user', sa.Column('role', role_enum, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')

    gender_enum.drop(op.get_bind())
    role_enum.drop(op.get_bind())
    # ### end Alembic commands ###