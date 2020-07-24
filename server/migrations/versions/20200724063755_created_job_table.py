"""Created job table

Revision ID: 6ac77d94b04a
Revises: 10225403a36e
Create Date: 2020-07-24 06:37:55.077045

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6ac77d94b04a'
down_revision = '10225403a36e'
branch_labels = None
depends_on = None

job_type_enum = postgresql.ENUM('contract_interim', 'contract_temp', 'permanent',
                                'part_time', 'temporary_seasonal', 'other',
                                'any', name='enum_job_type')


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    job_type_enum.create(op.get_bind())

    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Text(), nullable=True),
    sa.Column('company_name', sa.Text(), nullable=True),
    sa.Column('job_description', sa.Text(), nullable=True),
    sa.Column('job_title', sa.Text(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('post_date', sa.Date(), nullable=True),
    sa.Column('salary_offered', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.add_column('job', sa.Column('job_type', job_type_enum, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    job_type_enum.drop(op.get_bind())
    # ### end Alembic commands ###