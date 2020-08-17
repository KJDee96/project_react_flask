"""initial migration

Revision ID: d150db14c6b1
Revises: 
Create Date: 2020-08-13 21:16:39.111338

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd150db14c6b1'
down_revision = None
branch_labels = None
depends_on = None

gender_enum = postgresql.ENUM('male', 'female', 'other', name='enum_gender')
role_enum = postgresql.ENUM('candidate', 'employer', name='enum_role')


def upgrade():
    gender_enum.create(op.get_bind())
    role_enum.create(op.get_bind())

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('job_title', sa.Text(), nullable=True),
                    sa.Column('job_description', sa.Text(), nullable=True),
                    sa.Column('requirements', sa.Text(), nullable=True),
                    sa.Column('city', sa.Text(), nullable=True),
                    sa.Column('state', sa.Text(), nullable=True),
                    sa.Column('country', sa.Text(), nullable=True),
                    sa.Column('zipcode', sa.Text(), nullable=True),
                    sa.Column('start_date', sa.Date(), nullable=True),
                    sa.Column('end_date', sa.Date(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=50), nullable=True),
                    sa.Column('password', sa.Text(), nullable=True),
                    sa.Column('first_name', sa.Text(), nullable=True),
                    sa.Column('last_name', sa.Text(), nullable=True),
                    sa.Column('email', sa.Text(), nullable=True),
                    sa.Column('city', sa.Text(), nullable=True),
                    sa.Column('state', sa.Text(), nullable=True),
                    sa.Column('country', sa.Text(), nullable=True),
                    sa.Column('zipcode', sa.Text(), nullable=True),
                    sa.Column('degree_type', sa.Text(), nullable=True),
                    sa.Column('major', sa.Text(), nullable=True),
                    sa.Column('graduation_date', sa.Date(), nullable=True),
                    sa.Column('work_history_count', sa.Integer(), nullable=True),
                    sa.Column('work_history_years_experience', sa.Integer(), nullable=True),
                    sa.Column('employed', sa.Boolean(), nullable=True),
                    sa.Column('managed_others', sa.Boolean(), nullable=True),
                    sa.Column('managed_how_many', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.add_column('user', sa.Column('gender', gender_enum, nullable=True))
    op.add_column('user', sa.Column('role', role_enum, nullable=True))

    op.create_table('application',
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('job_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application')
    op.drop_table('user')
    op.drop_table('job')

    gender_enum.drop(op.get_bind())
    role_enum.drop(op.get_bind())

    # ### end Alembic commands ###